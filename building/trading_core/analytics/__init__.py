"""Analytics module for trading system."""

from .metrics import (
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
    drawdown_series,
    PerformanceMetrics,
)
from .mafe import MAFE, calculate_mae_mfe

__all__ = [
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
    "drawdown_series",
    "PerformanceMetrics",
    "MAFE",
    "calculate_mae_mfe",
]
