"""Example strategies for the MVP backtest harness.

Each strategy is a pure callable: (BarContext) -> Signal | None.
"""

from __future__ import annotations

from typing import Callable, Optional

import pandas as pd

from trading_core.backtest.harness import BarContext, Signal


def sma_cross_strategy(
    fast: int = 10, slow: int = 30
) -> Callable[[BarContext], Optional[Signal]]:
    """SMA fast/slow crossover.

    Generates BUY on fast-cross-above-slow, SELL on fast-cross-below-slow.
    Returns a closure compatible with Backtester.

    Args:
        fast: Fast SMA window.
        slow: Slow SMA window.

    Returns:
        Strategy callable.
    """
    if fast >= slow:
        raise ValueError("fast must be < slow")

    def strategy(ctx: BarContext) -> Optional[Signal]:
        if ctx.idx < slow:
            return None

        closes: pd.Series = ctx.history["close"]
        fast_now = closes.iloc[-fast:].mean()
        slow_now = closes.iloc[-slow:].mean()
        fast_prev = closes.iloc[-fast - 1 : -1].mean()
        slow_prev = closes.iloc[-slow - 1 : -1].mean()

        crossed_up = fast_prev <= slow_prev and fast_now > slow_now
        crossed_down = fast_prev >= slow_prev and fast_now < slow_now

        if crossed_up:
            return Signal.BUY
        if crossed_down:
            return Signal.SELL
        return None

    return strategy
