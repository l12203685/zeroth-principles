"""Backtest harness core.

Design:
- Strategy is a pure callable: (BarContext) -> Signal | None.
- Signals: BUY / SELL / CLOSE.  One position at a time, fixed size (MVP).
- Fills at current bar close, commission as fraction of notional, zero slippage.
- No margin, no partial fills, no limit/stop orders. MVP.

Immutable result objects (frozen dataclasses) where practical.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, List, Optional

import numpy as np
import pandas as pd

from trading_core.analytics.metrics import PerformanceMetrics

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Value objects
# ---------------------------------------------------------------------------


class Signal(str, Enum):
    """Strategy output per bar."""

    BUY = "BUY"      # Open long (flat -> long). No-op if already long.
    SELL = "SELL"    # Open short (flat -> short). No-op if already short.
    CLOSE = "CLOSE"  # Close any open position. No-op if flat.


@dataclass(frozen=True)
class BacktestConfig:
    """Backtest parameters.

    Attributes:
        initial_capital: Starting cash.
        commission_rate: Per-side commission as fraction of notional
            (0.001 = 0.1%).  Applied on entry AND exit.
        slippage_bps: Slippage in basis points (MVP: ignored, reserved).
        size: Fixed contract/share quantity per trade (MVP).
    """

    initial_capital: float = 100_000.0
    commission_rate: float = 0.001
    slippage_bps: float = 0.0
    size: float = 1.0


@dataclass(frozen=True)
class Trade:
    """Completed round-trip trade."""

    entry_time: pd.Timestamp
    exit_time: pd.Timestamp
    direction: str  # "long" | "short"
    size: float
    entry_price: float
    exit_price: float
    commission: float  # total commission (entry + exit)
    pnl: float  # net P&L after commission

    def to_dict(self) -> dict:
        return {
            "entry_time": self.entry_time,
            "exit_time": self.exit_time,
            "direction": self.direction,
            "size": self.size,
            "entry_price": self.entry_price,
            "exit_price": self.exit_price,
            "commission": self.commission,
            "pnl": self.pnl,
        }


@dataclass(frozen=True)
class BarContext:
    """Snapshot handed to the strategy callable on each bar.

    Strategy reads history (all bars up to and including `idx`) and returns
    a Signal or None. Strategies are pure: no side effects, no fills.
    """

    idx: int
    timestamp: pd.Timestamp
    bar: pd.Series
    history: pd.DataFrame  # rows [0 .. idx], inclusive
    position: str  # "flat" | "long" | "short"


@dataclass
class BacktestResult:
    """Backtest output bundle.

    Not frozen because pandas objects inside are mutable; treat as read-only.
    """

    equity_curve: pd.Series
    trade_log: pd.DataFrame
    metrics: PerformanceMetrics
    returns: pd.Series
    config: BacktestConfig

    def summary(self) -> str:
        return (
            f"Backtest: {len(self.trade_log)} trades, "
            f"final_equity={self.equity_curve.iloc[-1]:.2f}, "
            f"total_return="
            f"{(self.equity_curve.iloc[-1] / self.config.initial_capital - 1):.2%}\n"
            f"{self.metrics}"
        )


# ---------------------------------------------------------------------------
# Backtester
# ---------------------------------------------------------------------------


StrategyFn = Callable[[BarContext], Optional[Signal]]


class Backtester:
    """Minimal event-loop backtester.

    Usage:
        bt = Backtester(ohlcv, strategy_fn, BacktestConfig())
        result = bt.run()
        result.equity_curve  # pd.Series
        result.trade_log     # pd.DataFrame
        result.metrics       # PerformanceMetrics
    """

    _REQUIRED_COLS = ("open", "high", "low", "close", "volume")

    def __init__(
        self,
        ohlcv: pd.DataFrame,
        strategy: StrategyFn,
        config: Optional[BacktestConfig] = None,
    ) -> None:
        self._validate_ohlcv(ohlcv)
        self._ohlcv = ohlcv.sort_index()
        self._strategy = strategy
        self._config = config or BacktestConfig()

        # Runtime state (reset on run())
        self._position: str = "flat"  # "flat" | "long" | "short"
        self._entry_price: float = 0.0
        self._entry_time: Optional[pd.Timestamp] = None
        self._entry_commission: float = 0.0
        self._size: float = 0.0
        self._cash: float = 0.0
        self._trades: List[Trade] = []
        self._equity: List[float] = []

    @classmethod
    def _validate_ohlcv(cls, df: pd.DataFrame) -> None:
        missing = [c for c in cls._REQUIRED_COLS if c not in df.columns]
        if missing:
            raise ValueError(f"OHLCV missing columns: {missing}")
        if len(df) == 0:
            raise ValueError("OHLCV is empty")

    # ---- main loop -----------------------------------------------------

    def run(self) -> BacktestResult:
        """Execute backtest and return result bundle."""
        self._reset()

        for idx in range(len(self._ohlcv)):
            bar = self._ohlcv.iloc[idx]
            ts = self._ohlcv.index[idx]

            ctx = BarContext(
                idx=idx,
                timestamp=ts,
                bar=bar,
                history=self._ohlcv.iloc[: idx + 1],
                position=self._position,
            )

            signal = self._strategy(ctx)
            if signal is not None:
                self._apply_signal(signal, bar, ts)

            # Mark-to-market equity at bar close
            self._equity.append(self._mark_to_market(bar["close"]))

        # Force-close any open position at the last bar close (MVP policy)
        if self._position != "flat":
            last_ts = self._ohlcv.index[-1]
            last_close = float(self._ohlcv.iloc[-1]["close"])
            self._close_position(last_close, last_ts)
            # Update final equity to reflect realized close
            self._equity[-1] = self._cash

        return self._build_result()

    # ---- state mutators (private) --------------------------------------

    def _reset(self) -> None:
        self._position = "flat"
        self._entry_price = 0.0
        self._entry_time = None
        self._entry_commission = 0.0
        self._size = 0.0
        self._cash = float(self._config.initial_capital)
        self._trades = []
        self._equity = []

    def _apply_signal(
        self, signal: Signal, bar: pd.Series, ts: pd.Timestamp
    ) -> None:
        price = float(bar["close"])

        if signal == Signal.BUY:
            if self._position == "short":
                self._close_position(price, ts)
            if self._position == "flat":
                self._open_position("long", price, ts)

        elif signal == Signal.SELL:
            if self._position == "long":
                self._close_position(price, ts)
            if self._position == "flat":
                self._open_position("short", price, ts)

        elif signal == Signal.CLOSE:
            if self._position != "flat":
                self._close_position(price, ts)

    def _open_position(
        self, direction: str, price: float, ts: pd.Timestamp
    ) -> None:
        size = float(self._config.size)
        notional = price * size
        commission = notional * self._config.commission_rate

        # Cash accounting: debit commission only (position value is tracked
        # via mark-to-market). Keeps MVP simple; no margin modeling.
        self._cash -= commission

        self._position = direction
        self._entry_price = price
        self._entry_time = ts
        self._entry_commission = commission
        self._size = size

    def _close_position(self, price: float, ts: pd.Timestamp) -> None:
        size = self._size
        notional = price * size
        exit_commission = notional * self._config.commission_rate

        if self._position == "long":
            gross = (price - self._entry_price) * size
        else:  # short
            gross = (self._entry_price - price) * size

        total_commission = self._entry_commission + exit_commission
        pnl = gross - exit_commission  # entry commission already debited

        self._cash += pnl  # realize P&L minus exit commission

        trade = Trade(
            entry_time=self._entry_time,
            exit_time=ts,
            direction=self._position,
            size=size,
            entry_price=self._entry_price,
            exit_price=price,
            commission=total_commission,
            pnl=gross - total_commission,  # net of both commissions
        )
        self._trades.append(trade)

        # Reset position state
        self._position = "flat"
        self._entry_price = 0.0
        self._entry_time = None
        self._entry_commission = 0.0
        self._size = 0.0

    def _mark_to_market(self, price: float) -> float:
        """Equity = cash + unrealized P&L on open position."""
        if self._position == "flat":
            return self._cash
        if self._position == "long":
            unrealized = (price - self._entry_price) * self._size
        else:
            unrealized = (self._entry_price - price) * self._size
        return self._cash + unrealized

    # ---- result packaging ----------------------------------------------

    def _build_result(self) -> BacktestResult:
        equity = pd.Series(
            self._equity, index=self._ohlcv.index, name="equity"
        )
        returns = equity.pct_change().fillna(0.0)
        returns.name = "returns"

        trade_log = pd.DataFrame([t.to_dict() for t in self._trades])

        metrics = PerformanceMetrics.calculate(
            returns, trade_count=len(self._trades)
        )

        return BacktestResult(
            equity_curve=equity,
            trade_log=trade_log,
            metrics=metrics,
            returns=returns,
            config=self._config,
        )
