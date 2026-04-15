"""Backtest harness (M2 MVP).

Minimal, self-contained backtest framework:
- Feed historical OHLCV + strategy callable -> equity curve, trade log, metrics.
- Market-order fills at bar close, configurable commission, zero slippage.
- Decoupled from `trading_core.strategy.BaseStrategy` (no broker deps).

Public API:
    from trading_core.backtest import (
        Backtester,
        BacktestConfig,
        BacktestResult,
        Signal,
        Trade,
        sma_cross_strategy,
    )
"""

from trading_core.backtest.harness import (
    Backtester,
    BacktestConfig,
    BacktestResult,
    Signal,
    Trade,
    BarContext,
)
from trading_core.backtest.strategies import sma_cross_strategy

__all__ = [
    "Backtester",
    "BacktestConfig",
    "BacktestResult",
    "Signal",
    "Trade",
    "BarContext",
    "sma_cross_strategy",
]
