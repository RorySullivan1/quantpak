"""
Backtesting framework for strategy evaluation and performance analysis.

This module provides:
- Backtesting engine for strategy evaluation
- Portfolio simulation and tracking
- Transaction cost modeling
- Performance metrics calculation
- Risk management integration
"""

from .engine import BacktestEngine
from .portfolio import Portfolio
from .broker import Broker
from .metrics import PerformanceMetrics

__all__ = [
    "BacktestEngine",
    "Portfolio", 
    "Broker",
    "PerformanceMetrics",
]