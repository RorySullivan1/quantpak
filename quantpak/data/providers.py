"""
Financial data providers for various market data sources.
"""

import pandas as pd
import yfinance as yf
from abc import ABC, abstractmethod
from typing import List, Optional, Union, Dict, Any
from datetime import datetime, timedelta


class BaseProvider(ABC):
    """Base class for all data providers."""
    
    @abstractmethod
    def get_data(self, symbols: Union[str, List[str]], **kwargs) -> pd.DataFrame:
        """Fetch data for given symbols."""
        pass


class YahooProvider(BaseProvider):
    """Yahoo Finance data provider."""
    
    def __init__(self):
        self.name = "Yahoo Finance"
    
    def get_data(
        self, 
        symbols: Union[str, List[str]], 
        start: Optional[str] = None,
        end: Optional[str] = None,
        period: str = "1y",
        interval: str = "1d"
    ) -> pd.DataFrame:
        """
        Fetch data from Yahoo Finance.
        
        Args:
            symbols: Stock symbols to fetch
            start: Start date (YYYY-MM-DD)
            end: End date (YYYY-MM-DD)
            period: Period to fetch (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
            interval: Data interval (1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo)
        
        Returns:
            DataFrame with OHLCV data
        """
        ticker = yf.Ticker(symbols) if isinstance(symbols, str) else yf.Tickers(symbols)
        
        if start and end:
            data = ticker.history(start=start, end=end, interval=interval)
        else:
            data = ticker.history(period=period, interval=interval)
            
        return data
    
    def get_info(self, symbol: str) -> Dict[str, Any]:
        """Get company information."""
        ticker = yf.Ticker(symbol)
        return ticker.info
    
    def get_financials(self, symbol: str) -> Dict[str, pd.DataFrame]:
        """Get financial statements."""
        ticker = yf.Ticker(symbol)
        return {
            'income_statement': ticker.financials,
            'balance_sheet': ticker.balance_sheet,
            'cash_flow': ticker.cashflow
        }


class AlphaVantageProvider(BaseProvider):
    """Alpha Vantage data provider."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.name = "Alpha Vantage"
    
    def get_data(self, symbols: Union[str, List[str]], **kwargs) -> pd.DataFrame:
        """Fetch data from Alpha Vantage."""
        # Implementation would use alpha_vantage library
        raise NotImplementedError("Alpha Vantage provider implementation pending")


class FREDProvider(BaseProvider):
    """Federal Reserve Economic Data provider."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.name = "FRED"
    
    def get_data(self, symbols: Union[str, List[str]], **kwargs) -> pd.DataFrame:
        """Fetch economic data from FRED."""
        # Implementation would use fredapi
        raise NotImplementedError("FRED provider implementation pending")


class QuandlProvider(BaseProvider):
    """Quandl data provider."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.name = "Quandl"
    
    def get_data(self, symbols: Union[str, List[str]], **kwargs) -> pd.DataFrame:
        """Fetch data from Quandl."""
        # Implementation would use quandl library
        raise NotImplementedError("Quandl provider implementation pending")