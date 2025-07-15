"""
Data processing utilities for financial data cleaning, transformation, and technical analysis.
"""

import pandas as pd
import numpy as np
from typing import Union, Optional, Dict, Any


class DataProcessor:
    """General data processing utilities."""
    
    @staticmethod
    def clean_data(df: pd.DataFrame) -> pd.DataFrame:
        """Clean financial data by handling missing values and outliers."""
        # Remove rows with all NaN values
        df = df.dropna(how='all')
        
        # Forward fill missing values for price data
        price_cols = ['Open', 'High', 'Low', 'Close', 'Adj Close']
        for col in price_cols:
            if col in df.columns:
                df[col] = df[col].fillna(method='ffill')
        
        # Handle volume separately (fill with 0)
        if 'Volume' in df.columns:
            df['Volume'] = df['Volume'].fillna(0)
            
        return df
    
    @staticmethod
    def resample_data(df: pd.DataFrame, freq: str) -> pd.DataFrame:
        """Resample data to different frequency."""
        agg_dict = {
            'Open': 'first',
            'High': 'max',
            'Low': 'min',
            'Close': 'last',
            'Adj Close': 'last',
            'Volume': 'sum'
        }
        
        # Only include columns that exist in the dataframe
        agg_dict = {k: v for k, v in agg_dict.items() if k in df.columns}
        
        return df.resample(freq).agg(agg_dict)


class ReturnCalculator:
    """Calculate various types of returns and risk metrics."""
    
    @staticmethod
    def simple_returns(prices: pd.Series) -> pd.Series:
        """Calculate simple returns."""
        return prices.pct_change()
    
    @staticmethod
    def log_returns(prices: pd.Series) -> pd.Series:
        """Calculate logarithmic returns."""
        return np.log(prices / prices.shift(1))
    
    @staticmethod
    def cumulative_returns(returns: pd.Series) -> pd.Series:
        """Calculate cumulative returns."""
        return (1 + returns).cumprod() - 1
    
    @staticmethod
    def rolling_volatility(returns: pd.Series, window: int = 30) -> pd.Series:
        """Calculate rolling volatility (annualized)."""
        return returns.rolling(window=window).std() * np.sqrt(252)
    
    @staticmethod
    def sharpe_ratio(returns: pd.Series, risk_free_rate: float = 0.02) -> float:
        """Calculate Sharpe ratio."""
        excess_returns = returns.mean() * 252 - risk_free_rate
        volatility = returns.std() * np.sqrt(252)
        return excess_returns / volatility if volatility != 0 else 0


class TechnicalIndicators:
    """Technical analysis indicators."""
    
    @staticmethod
    def sma(prices: pd.Series, window: int) -> pd.Series:
        """Simple Moving Average."""
        return prices.rolling(window=window).mean()
    
    @staticmethod
    def ema(prices: pd.Series, window: int) -> pd.Series:
        """Exponential Moving Average."""
        return prices.ewm(span=window).mean()
    
    @staticmethod
    def bollinger_bands(prices: pd.Series, window: int = 20, num_std: float = 2) -> Dict[str, pd.Series]:
        """Bollinger Bands."""
        sma = prices.rolling(window=window).mean()
        std = prices.rolling(window=window).std()
        
        return {
            'middle': sma,
            'upper': sma + (std * num_std),
            'lower': sma - (std * num_std)
        }
    
    @staticmethod
    def rsi(prices: pd.Series, window: int = 14) -> pd.Series:
        """Relative Strength Index."""
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi
    
    @staticmethod
    def macd(prices: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9) -> Dict[str, pd.Series]:
        """MACD indicator."""
        ema_fast = prices.ewm(span=fast).mean()
        ema_slow = prices.ewm(span=slow).mean()
        macd_line = ema_fast - ema_slow
        signal_line = macd_line.ewm(span=signal).mean()
        histogram = macd_line - signal_line
        
        return {
            'macd': macd_line,
            'signal': signal_line,
            'histogram': histogram
        }