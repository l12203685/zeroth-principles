"""Strategy module for trading system."""

from .base import BaseStrategy
from .strategies_extended import (
    CCIConfig,
    CCIStrategy,
    DMIConfig,
    DMIStrategy,
    KeltnerConfig,
    KeltnerStrategy,
    MACDConfig,
    MACDStrategy,
    ORBConfig,
    ORBStrategy,
)
from .pla_catalog import PLAPattern, PLA_CATALOG, StrategyGenerator
from .performance_tracker import (
    PerformanceTracker,
    StrategyPerf,
    correlation_matrix,
    edge_ratio,
    rolling_sharpe,
)

__all__ = [
    "BaseStrategy",
    # extended strategies
    "CCIConfig",
    "CCIStrategy",
    "DMIConfig",
    "DMIStrategy",
    "KeltnerConfig",
    "KeltnerStrategy",
    "MACDConfig",
    "MACDStrategy",
    "ORBConfig",
    "ORBStrategy",
    # catalog
    "PLAPattern",
    "PLA_CATALOG",
    "StrategyGenerator",
    # performance tracker
    "PerformanceTracker",
    "StrategyPerf",
    "correlation_matrix",
    "edge_ratio",
    "rolling_sharpe",
]
