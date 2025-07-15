"""
Trading strategies and signal generation framework.

This module provides:
- Base strategy class and framework
- Technical analysis strategies
- Momentum and mean reversion strategies
- Multi-factor strategies
- Machine learning strategies
"""

from .base import BaseStrategy
from .technical import (
    MovingAverageCrossover,
    RSIStrategy,
    BollingerBandsStrategy,
    MACDStrategy,
)
from .momentum import (
    MomentumStrategy,
    PairsTrading,
)
from .mean_reversion import (
    MeanReversionStrategy,
    StatisticalArbitrage,
)

__all__ = [
    "BaseStrategy",
    "MovingAverageCrossover",
    "RSIStrategy", 
    "BollingerBandsStrategy",
    "MACDStrategy",
    "MomentumStrategy",
    "PairsTrading",
    "MeanReversionStrategy",
    "StatisticalArbitrage",
]