"""
QuantPak - A comprehensive quantitative finance package for analysis, backtesting, and visualization.

This package provides tools for:
- Financial data acquisition and processing
- Strategy development and backtesting
- Portfolio optimization and risk management
- Performance analysis and visualization
- Factor modeling and forecasting
"""

__version__ = "0.1.0"
__author__ = "QuantPak Development Team"

# Core imports
from . import data
from . import strategies
from . import backtesting
from . import portfolio
from . import risk
from . import performance
from . import models
from . import stats
from . import visuals
from . import utils
from . import datatypes

__all__ = [
    "data",
    "strategies", 
    "backtesting",
    "portfolio",
    "risk", 
    "performance",
    "models",
    "stats",
    "visuals",
    "utils",
    "datatypes",
]