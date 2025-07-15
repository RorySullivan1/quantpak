"""
Base strategy class and framework for developing trading strategies.
"""

import pandas as pd
import numpy as np
from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass
from enum import Enum


class SignalType(Enum):
    """Trading signal types."""
    BUY = 1
    SELL = -1
    HOLD = 0


@dataclass
class Signal:
    """Trading signal data structure."""
    timestamp: pd.Timestamp
    symbol: str
    signal_type: SignalType
    strength: float = 1.0
    price: Optional[float] = None
    metadata: Optional[Dict[str, Any]] = None


class BaseStrategy(ABC):
    """
    Base class for all trading strategies.
    
    This class provides the framework for developing and implementing
    trading strategies with standardized signal generation and parameter management.
    """
    
    def __init__(self, name: str, parameters: Optional[Dict[str, Any]] = None):
        self.name = name
        self.parameters = parameters or {}
        self.signals = []
        self.data = None
        self.initialized = False
    
    @abstractmethod
    def generate_signals(self, data: pd.DataFrame) -> List[Signal]:
        """
        Generate trading signals based on input data.
        
        Args:
            data: OHLCV price data
            
        Returns:
            List of trading signals
        """
        pass
    
    def initialize(self, data: pd.DataFrame) -> None:
        """
        Initialize strategy with historical data.
        
        Args:
            data: Historical OHLCV data
        """
        self.data = data
        self.initialized = True
    
    def update(self, new_data: pd.Series) -> Optional[Signal]:
        """
        Update strategy with new data point and generate signal if needed.
        
        Args:
            new_data: New data point
            
        Returns:
            Trading signal if generated, None otherwise
        """
        if not self.initialized:
            raise ValueError("Strategy must be initialized before updating")
        
        # Append new data
        self.data = pd.concat([self.data, new_data.to_frame().T])
        
        # Generate signal for latest data
        signals = self.generate_signals(self.data.tail(1))
        return signals[0] if signals else None
    
    def get_parameter(self, key: str, default: Any = None) -> Any:
        """Get strategy parameter."""
        return self.parameters.get(key, default)
    
    def set_parameter(self, key: str, value: Any) -> None:
        """Set strategy parameter."""
        self.parameters[key] = value
    
    def validate_data(self, data: pd.DataFrame) -> bool:
        """
        Validate input data format and requirements.
        
        Args:
            data: Input data to validate
            
        Returns:
            True if data is valid
        """
        required_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
        return all(col in data.columns for col in required_columns)
    
    def calculate_indicators(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate technical indicators for the strategy.
        Override in subclasses to add specific indicators.
        
        Args:
            data: OHLCV data
            
        Returns:
            DataFrame with additional indicator columns
        """
        return data.copy()
    
    def get_signals_dataframe(self) -> pd.DataFrame:
        """Convert signals list to DataFrame for analysis."""
        if not self.signals:
            return pd.DataFrame()
        
        signal_data = []
        for signal in self.signals:
            signal_data.append({
                'timestamp': signal.timestamp,
                'symbol': signal.symbol,
                'signal': signal.signal_type.value,
                'strength': signal.strength,
                'price': signal.price
            })
        
        return pd.DataFrame(signal_data).set_index('timestamp')
    
    def performance_summary(self) -> Dict[str, Any]:
        """
        Generate performance summary for the strategy.
        
        Returns:
            Dictionary with performance metrics
        """
        signals_df = self.get_signals_dataframe()
        
        if signals_df.empty:
            return {"total_signals": 0}
        
        buy_signals = len(signals_df[signals_df['signal'] == 1])
        sell_signals = len(signals_df[signals_df['signal'] == -1])
        
        return {
            "total_signals": len(signals_df),
            "buy_signals": buy_signals,
            "sell_signals": sell_signals,
            "signal_frequency": len(signals_df) / len(self.data) if self.data is not None else 0
        }