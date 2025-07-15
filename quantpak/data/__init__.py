"""
Data module for financial data acquisition, processing, and management.

This module provides:
- Market data providers (Yahoo Finance, Alpha Vantage, FRED, etc.)
- Data processing and cleaning utilities
- Data storage and caching mechanisms
- Real-time data streaming capabilities
"""

from .providers import (
    YahooProvider,
    AlphaVantageProvider,
    FREDProvider,
    QuandlProvider,
)
from .processors import (
    DataProcessor,
    ReturnCalculator,
    TechnicalIndicators,
)
from .storage import (
    DataStorage,
    CacheManager,
)

__all__ = [
    "YahooProvider",
    "AlphaVantageProvider", 
    "FREDProvider",
    "QuandlProvider",
    "DataProcessor",
    "ReturnCalculator",
    "TechnicalIndicators",
    "DataStorage",
    "CacheManager",
]