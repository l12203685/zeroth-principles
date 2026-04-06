"""Trading Core - Unified Quantitative Trading System.

Merged and unified codebase from:
- AlgoTrading (78 .py files)
- PYMAFE (5 .py files)
- sino-trade-api (9 .py files)

Clean, modular architecture for backtesting and live trading with Sinopac broker.
"""

__version__ = "1.0.0"
__author__ = "Edward"

from trading_core.config import Settings, get_settings
from trading_core.broker import get_api, BrokerConnector
from trading_core.data import (
    get_ohlcv,
    get_tick_data,
    resample_ohlcv,
    Portfolio,
    Position,
)
from trading_core.analytics import (
    sharpe_ratio,
    sortino_ratio,
    max_drawdown,
    calmar_ratio,
    win_rate,
    profit_factor,
    recovery_factor,
    sqn,
    mar,
    annual_return,
    PerformanceMetrics,
    MAFE,
    calculate_mae_mfe,
)
from trading_core.strategy import BaseStrategy

__all__ = [
    # Config
    "Settings",
    "get_settings",
    # Broker
    "get_api",
    "BrokerConnector",
    # Data
    "get_ohlcv",
    "get_tick_data",
    "resample_ohlcv",
    "Portfolio",
    "Position",
    # Analytics
    "sharpe_ratio",
    "sortino_ratio",
    "max_drawdown",
    "calmar_ratio",
    "win_rate",
    "profit_factor",
    "recovery_factor",
    "sqn",
    "mar",
    "annual_return",
    "PerformanceMetrics",
    "MAFE",
    "calculate_mae_mfe",
    # Strategy
    "BaseStrategy",
]
