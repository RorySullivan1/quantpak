"""
Performance analysis and attribution framework.

This module provides:
- Performance metrics calculation
- Benchmark comparison and attribution
- Factor attribution analysis
- Risk-adjusted performance measures
- Performance reporting and visualization
"""

from .metrics import (
    PerformanceMetrics,
    RiskAdjustedMetrics,
    BenchmarkAnalysis,
)
from .attribution import (
    AttributionAnalysis,
    FactorAttribution,
)
from .reporting import PerformanceReporter

__all__ = [
    "PerformanceMetrics",
    "RiskAdjustedMetrics", 
    "BenchmarkAnalysis",
    "AttributionAnalysis",
    "FactorAttribution",
    "PerformanceReporter",
]