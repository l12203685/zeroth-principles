"""Backtest package.

Two engines available:

MVP harness (harness.py)
------------------------
Minimal, self-contained: fills at bar close, fraction-of-notional commission,
zero slippage, fixed size.

    from trading_core.backtest import Backtester, BacktestConfig

Advanced engine (engine.py)
----------------------------
Full fee/slippage/sizing + PaperOrderManager integration:
- Commission: fraction-of-notional OR flat per-contract.
- Slippage: none, fixed-ticks, or percentage.
- Sizing: fixed, percent-of-equity, or fractional-Kelly.
- Fills at next-bar open for realism.

    from trading_core.backtest import (
        BacktestEngine,
        EngineConfig,
        CommissionMode,
        SlippageMode,
        SizingMode,
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
from trading_core.backtest.engine import (
    BacktestEngine,
    EngineConfig,
    CommissionMode,
    SlippageMode,
    SizingMode,
)

__all__ = [
    # MVP harness
    "Backtester",
    "BacktestConfig",
    "BacktestResult",
    "Signal",
    "Trade",
    "BarContext",
    "sma_cross_strategy",
    # Advanced engine
    "BacktestEngine",
    "EngineConfig",
    "CommissionMode",
    "SlippageMode",
    "SizingMode",
]
