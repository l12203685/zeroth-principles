"""Advanced backtest engine with fee, slippage, and capital-efficiency features.

Extends the MVP ``Backtester`` (harness.py) with:

- **Commission modes**: per-trade fraction-of-notional *or* flat per-contract.
- **Slippage models**: fixed-tick or percentage-of-price.
- **Position sizing**: fixed, percent-of-equity, or fractional-Kelly.
- **PaperOrderManager integration**: every fill goes through the order manager
  so order lifecycle is tracked identically to live trading.
- **BacktestResult**: equity_curve, trade_log, metrics (Sharpe, MDD, PF,
  win_rate, Sortino, Calmar, SQN, annual_return).

Design principles
-----------------
- Immutable config and result objects (frozen dataclasses).
- No mutation of input data.
- Pure strategy callable: ``(BarContext) -> Signal | None``.
- Fills at next-bar open + slippage (more realistic than close-fill MVP).
  Falls back to bar close when bar open is unavailable.
- One position at a time per symbol.

Public API
----------
::

    from trading_core.backtest.engine import (
        BacktestEngine,
        EngineConfig,
        CommissionMode,
        SlippageMode,
        SizingMode,
        BacktestResult,
    )

    config = EngineConfig(
        initial_capital=1_000_000.0,
        commission_mode=CommissionMode.PER_CONTRACT,
        commission_value=100.0,       # NT$100 per contract round-turn
        slippage_mode=SlippageMode.FIXED_TICKS,
        slippage_value=1.0,           # 1 tick
        tick_size=1.0,
        sizing_mode=SizingMode.PERCENT_EQUITY,
        sizing_param=0.02,            # 2% equity per trade
        price_per_unit=200_000.0,     # TXF: each pt worth NT$200 * multiplier
    )

    engine = BacktestEngine(ohlcv, strategy_fn, config)
    result = engine.run()
    print(result.summary())
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Dict, List, Optional

import numpy as np
import pandas as pd

from trading_core.analytics.metrics import PerformanceMetrics
from trading_core.backtest.harness import BarContext, BacktestResult, Signal, Trade
from trading_core.broker.orders import (
    Order,
    OrderSide,
    OrderType,
    PaperOrderManager,
)

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Configuration enums
# ---------------------------------------------------------------------------


class CommissionMode(str, Enum):
    """How commission is calculated per trade."""

    FRACTION_OF_NOTIONAL = "fraction_of_notional"
    """commission_value is a fraction (e.g. 0.001 = 0.1%) of notional traded."""

    PER_CONTRACT = "per_contract"
    """commission_value is a flat amount per contract (round-turn per trade)."""


class SlippageMode(str, Enum):
    """How slippage is applied to fill prices."""

    NONE = "none"
    """No slippage applied."""

    FIXED_TICKS = "fixed_ticks"
    """slippage_value is the number of ticks (multiplied by tick_size)."""

    PERCENT = "percent"
    """slippage_value is a fraction of fill price (e.g. 0.0005 = 0.05%)."""


class SizingMode(str, Enum):
    """How position size (number of contracts/shares) is determined."""

    FIXED = "fixed"
    """sizing_param is the fixed quantity per trade."""

    PERCENT_EQUITY = "percent_equity"
    """sizing_param is the fraction of current equity to risk (0 < p <= 1).
    Size = floor(equity * sizing_param / (fill_price * price_per_unit))."""

    KELLY = "kelly"
    """sizing_param is the Kelly fraction (0 < f <= 1).
    Full Kelly size = (win_rate * avg_win - loss_rate * avg_loss) / avg_loss.
    Actual size = full_kelly * sizing_param.  Requires at least 10 closed trades
    to activate; falls back to FIXED=1 before that."""


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class EngineConfig:
    """Full configuration for BacktestEngine.

    Attributes:
        initial_capital:   Starting cash in account currency.
        commission_mode:   How commission is computed.
        commission_value:  Parameter for commission_mode:
                           - FRACTION_OF_NOTIONAL: fraction (e.g. 0.001).
                           - PER_CONTRACT: flat amount per contract per side.
        slippage_mode:     How slippage is applied to fills.
        slippage_value:    Parameter for slippage_mode:
                           - FIXED_TICKS: number of ticks.
                           - PERCENT: fraction of price.
        tick_size:         Minimum price increment (used by FIXED_TICKS).
        sizing_mode:       How trade size (qty) is determined.
        sizing_param:      Parameter for sizing_mode:
                           - FIXED: quantity (default 1).
                           - PERCENT_EQUITY: fraction of equity (e.g. 0.02).
                           - KELLY: Kelly fraction multiplier (e.g. 0.5).
        price_per_unit:    Value of 1 price unit per contract in account
                           currency.  e.g. TXF = 200 (NT$200 per index point).
                           Used for equity-based sizing.  Set to 1.0 for stocks.
        max_size:          Hard cap on position size (contracts).  0 = no cap.
        min_size:          Minimum size; trades below this are skipped.
    """

    initial_capital: float = 1_000_000.0
    commission_mode: CommissionMode = CommissionMode.FRACTION_OF_NOTIONAL
    commission_value: float = 0.001
    slippage_mode: SlippageMode = SlippageMode.NONE
    slippage_value: float = 0.0
    tick_size: float = 1.0
    sizing_mode: SizingMode = SizingMode.FIXED
    sizing_param: float = 1.0
    price_per_unit: float = 1.0
    max_size: float = 0.0
    min_size: float = 1.0

    def __post_init__(self) -> None:
        if self.initial_capital <= 0:
            raise ValueError("initial_capital must be positive")
        if self.commission_value < 0:
            raise ValueError("commission_value must be >= 0")
        if self.slippage_value < 0:
            raise ValueError("slippage_value must be >= 0")
        if self.tick_size <= 0:
            raise ValueError("tick_size must be positive")
        if self.sizing_param <= 0:
            raise ValueError("sizing_param must be positive")
        if self.price_per_unit <= 0:
            raise ValueError("price_per_unit must be positive")
        if self.min_size <= 0:
            raise ValueError("min_size must be positive")


# ---------------------------------------------------------------------------
# Result container
# ---------------------------------------------------------------------------


@dataclass
class BacktestResult:
    """Complete backtest output.

    Attributes:
        equity_curve:  pd.Series indexed by bar timestamps.
        trade_log:     pd.DataFrame with one row per completed round-turn.
        metrics:       PerformanceMetrics (Sharpe, MDD, PF, win_rate, …).
        returns:       Bar-level percentage returns of equity curve.
        config:        The EngineConfig used.
        orders:        Dict of all Order objects created (order_id -> Order).
    """

    equity_curve: pd.Series
    trade_log: pd.DataFrame
    metrics: PerformanceMetrics
    returns: pd.Series
    config: EngineConfig
    orders: Dict[str, Order] = field(default_factory=dict)

    def summary(self) -> str:
        """Human-readable one-liner + metrics block."""
        n_trades = len(self.trade_log)
        final_eq = self.equity_curve.iloc[-1]
        total_ret = final_eq / self.config.initial_capital - 1
        return (
            f"BacktestEngine: {n_trades} trades, "
            f"final_equity={final_eq:,.2f}, "
            f"total_return={total_ret:.2%}\n"
            f"{self.metrics}"
        )


# ---------------------------------------------------------------------------
# Engine internals helpers
# ---------------------------------------------------------------------------


def _compute_commission(
    mode: CommissionMode,
    value: float,
    fill_price: float,
    quantity: float,
) -> float:
    """Compute one-side commission.

    Args:
        mode:        CommissionMode enum.
        value:       Commission parameter.
        fill_price:  Execution price.
        quantity:    Number of contracts.

    Returns:
        Commission amount in account currency.
    """
    if mode == CommissionMode.FRACTION_OF_NOTIONAL:
        return fill_price * quantity * value
    # PER_CONTRACT: flat fee per contract per side
    return quantity * value


def _apply_slippage(
    mode: SlippageMode,
    value: float,
    tick_size: float,
    raw_price: float,
    is_buy: bool,
) -> float:
    """Return fill price after slippage.

    Slippage always moves against the trader:
    - Buy  → fill price is higher than raw_price.
    - Sell → fill price is lower  than raw_price.

    Args:
        mode:       SlippageMode.
        value:      Slippage parameter.
        tick_size:  Price tick.
        raw_price:  Pre-slippage price.
        is_buy:     True for buys, False for sells.

    Returns:
        Adjusted fill price.
    """
    if mode == SlippageMode.NONE:
        return raw_price
    if mode == SlippageMode.FIXED_TICKS:
        slip_amount = value * tick_size
    else:  # PERCENT
        slip_amount = raw_price * value

    return raw_price + slip_amount if is_buy else raw_price - slip_amount


def _kelly_fraction(trades: List[dict]) -> float:
    """Estimate Kelly numerator/denominator from closed-trade P&L.

    Kelly = (win_rate * avg_win_pnl - loss_rate * avg_loss_pnl) / avg_win_pnl
    Clamped to [0, 2] to avoid extreme values.

    Args:
        trades: List of trade dicts with key "pnl".

    Returns:
        Kelly fraction in [0, 2].
    """
    pnls = np.array([t["pnl"] for t in trades])
    wins = pnls[pnls > 0]
    losses = pnls[pnls < 0]

    if len(wins) == 0 or len(losses) == 0:
        return 1.0  # no information → return 1× (will be scaled by sizing_param)

    win_rate = len(wins) / len(pnls)
    avg_win = wins.mean()
    avg_loss = abs(losses.mean())

    kelly = (win_rate * avg_win - (1 - win_rate) * avg_loss) / avg_win
    return float(np.clip(kelly, 0.0, 2.0))


def _compute_size(
    config: EngineConfig,
    equity: float,
    fill_price: float,
    closed_trades: List[dict],
) -> float:
    """Calculate trade size in contracts.

    Args:
        config:        EngineConfig with sizing parameters.
        equity:        Current mark-to-market equity.
        fill_price:    Expected fill price.
        closed_trades: History of closed trades for Kelly estimation.

    Returns:
        Number of contracts to trade (may be 0 if below min_size).
    """
    if config.sizing_mode == SizingMode.FIXED:
        size = config.sizing_param

    elif config.sizing_mode == SizingMode.PERCENT_EQUITY:
        unit_value = fill_price * config.price_per_unit
        if unit_value <= 0:
            return 0.0
        size = (equity * config.sizing_param) / unit_value
        size = max(0.0, size)

    else:  # KELLY
        # Need at least 10 trades to have a stable Kelly estimate
        if len(closed_trades) < 10:
            size = 1.0
        else:
            k = _kelly_fraction(closed_trades)
            unit_value = fill_price * config.price_per_unit
            if unit_value <= 0:
                return 0.0
            full_kelly_size = (equity * k) / unit_value
            size = max(0.0, full_kelly_size * config.sizing_param)

    # Apply hard cap
    if config.max_size > 0:
        size = min(size, config.max_size)

    # Floor to integers (contracts are discrete in futures)
    size = float(int(size))

    # Enforce minimum
    if size < config.min_size:
        return 0.0
    return size


# ---------------------------------------------------------------------------
# BacktestEngine
# ---------------------------------------------------------------------------


StrategyFn = Callable[[BarContext], Optional[Signal]]


class BacktestEngine:
    """Advanced event-loop backtester with fee/slippage/sizing + PaperOrderManager.

    Key improvements over MVP ``Backtester``:

    1. **Commission modes**: fraction-of-notional or flat per-contract.
    2. **Slippage**: none, fixed-ticks, or percentage.
    3. **Position sizing**: fixed, percent-of-equity, or Kelly.
    4. **Order tracking**: every fill is routed through PaperOrderManager so
       the full order lifecycle (place → fill → cancel) is recorded.
    5. **Fill price**: next bar open + slippage (more realistic); falls back
       to current bar close when bar open is not in the data.

    Usage::

        engine = BacktestEngine(ohlcv, my_strategy, EngineConfig(
            initial_capital=500_000,
            commission_mode=CommissionMode.PER_CONTRACT,
            commission_value=50.0,
            slippage_mode=SlippageMode.FIXED_TICKS,
            slippage_value=1.0,
        ))
        result = engine.run()

    Args:
        ohlcv:    DataFrame with columns open/high/low/close/volume, time index.
        strategy: Pure callable ``(BarContext) -> Signal | None``.
        config:   EngineConfig (defaults to MVP-compatible settings).
    """

    _REQUIRED_COLS = ("open", "high", "low", "close", "volume")

    def __init__(
        self,
        ohlcv: pd.DataFrame,
        strategy: StrategyFn,
        config: Optional[EngineConfig] = None,
    ) -> None:
        self._validate_ohlcv(ohlcv)
        self._ohlcv = ohlcv.sort_index().copy()
        self._strategy = strategy
        self._config = config or EngineConfig()

        # Runtime state (reset on each run() call)
        self._position: str = "flat"  # "flat" | "long" | "short"
        self._entry_price: float = 0.0
        self._entry_time: Optional[pd.Timestamp] = None
        self._entry_commission: float = 0.0
        self._size: float = 0.0
        self._cash: float = 0.0
        self._equity: List[float] = []
        self._trades: List[dict] = []
        self._paper_om: Optional[PaperOrderManager] = None
        self._pending_signal: Optional[Signal] = None
        self._pending_signal_bar_idx: int = -1

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    @classmethod
    def _validate_ohlcv(cls, df: pd.DataFrame) -> None:
        missing = [c for c in cls._REQUIRED_COLS if c not in df.columns]
        if missing:
            raise ValueError(f"OHLCV missing columns: {missing}")
        if len(df) == 0:
            raise ValueError("OHLCV DataFrame is empty")

    # ------------------------------------------------------------------
    # Main entry point
    # ------------------------------------------------------------------

    def run(self) -> BacktestResult:
        """Execute backtest over the full OHLCV history.

        Returns:
            BacktestResult with equity_curve, trade_log, metrics, orders.
        """
        self._reset()

        n = len(self._ohlcv)
        for idx in range(n):
            bar = self._ohlcv.iloc[idx]
            ts = self._ohlcv.index[idx]

            # ---- Step 1: execute any pending signal from the prior bar ----
            # Fills at *this* bar's open (next-bar open execution).
            if self._pending_signal is not None and self._pending_signal_bar_idx == idx:
                open_price = float(bar.get("open", bar["close"]))
                self._execute_signal(self._pending_signal, open_price, ts)
                self._pending_signal = None
                self._pending_signal_bar_idx = -1

            # ---- Step 2: call strategy on history up to this bar ----
            ctx = BarContext(
                idx=idx,
                timestamp=ts,
                bar=bar,
                history=self._ohlcv.iloc[: idx + 1],
                position=self._position,
            )
            signal = self._strategy(ctx)

            # Schedule signal for next-bar execution
            if signal is not None and idx + 1 < n:
                self._pending_signal = signal
                self._pending_signal_bar_idx = idx + 1
            elif signal is not None and idx + 1 >= n:
                # Last bar signal: execute immediately at close (no next bar)
                close_price = float(bar["close"])
                self._execute_signal(signal, close_price, ts)

            # ---- Step 3: mark-to-market at bar close ----
            self._equity.append(self._mark_to_market(float(bar["close"])))

        # ---- Force-close any open position at last bar close ----
        if self._position != "flat":
            last_ts = self._ohlcv.index[-1]
            last_close = float(self._ohlcv.iloc[-1]["close"])
            self._close_position(last_close, last_ts)
            self._equity[-1] = self._mark_to_market(last_close)

        return self._build_result()

    # ------------------------------------------------------------------
    # State mutators (private)
    # ------------------------------------------------------------------

    def _reset(self) -> None:
        """Reset all mutable state for a fresh run."""
        self._position = "flat"
        self._entry_price = 0.0
        self._entry_time = None
        self._entry_commission = 0.0
        self._size = 0.0
        self._cash = float(self._config.initial_capital)
        self._equity = []
        self._trades = []
        # auto_fill=False: we control fill prices via simulate_fill()
        self._paper_om = PaperOrderManager(auto_fill=False)
        self._pending_signal = None
        self._pending_signal_bar_idx = -1

    def _current_equity(self) -> float:
        """Mark-to-market equity at the most recently computed close."""
        if self._equity:
            return self._equity[-1]
        return self._cash

    def _execute_signal(
        self, signal: Signal, raw_price: float, ts: pd.Timestamp
    ) -> None:
        """Process a signal: open / close / flip position.

        Args:
            signal:    BUY, SELL, or CLOSE.
            raw_price: Pre-slippage reference price (usually bar open).
            ts:        Bar timestamp for recording.
        """
        if signal == Signal.BUY:
            if self._position == "short":
                close_price = _apply_slippage(
                    self._config.slippage_mode,
                    self._config.slippage_value,
                    self._config.tick_size,
                    raw_price,
                    is_buy=True,
                )
                self._close_position(close_price, ts)
            if self._position == "flat":
                entry_price = _apply_slippage(
                    self._config.slippage_mode,
                    self._config.slippage_value,
                    self._config.tick_size,
                    raw_price,
                    is_buy=True,
                )
                self._open_position("long", entry_price, ts)

        elif signal == Signal.SELL:
            if self._position == "long":
                close_price = _apply_slippage(
                    self._config.slippage_mode,
                    self._config.slippage_value,
                    self._config.tick_size,
                    raw_price,
                    is_buy=False,
                )
                self._close_position(close_price, ts)
            if self._position == "flat":
                entry_price = _apply_slippage(
                    self._config.slippage_mode,
                    self._config.slippage_value,
                    self._config.tick_size,
                    raw_price,
                    is_buy=False,
                )
                self._open_position("short", entry_price, ts)

        elif signal == Signal.CLOSE:
            if self._position != "flat":
                is_buy = self._position == "short"  # closing short = buying back
                close_price = _apply_slippage(
                    self._config.slippage_mode,
                    self._config.slippage_value,
                    self._config.tick_size,
                    raw_price,
                    is_buy=is_buy,
                )
                self._close_position(close_price, ts)

    def _open_position(
        self, direction: str, fill_price: float, ts: pd.Timestamp
    ) -> None:
        """Open a new position; route through PaperOrderManager.

        Args:
            direction:  "long" or "short".
            fill_price: Actual fill price (after slippage).
            ts:         Trade timestamp.
        """
        equity = self._current_equity()
        size = _compute_size(self._config, equity, fill_price, self._trades)

        if size <= 0:
            logger.debug("Skipped open at %s: computed size=0", ts)
            return

        # Place market order through PaperOrderManager (auto_fill=False so we
        # control the fill price after slippage adjustment).
        side = OrderSide.BUY.value if direction == "long" else OrderSide.SELL.value
        order = self._paper_om.place_order(
            symbol="BT",          # generic symbol for backtest
            side=side,
            quantity=size,
            order_type=OrderType.MARKET.value,
        )
        # Manually fill at the slippage-adjusted price
        if order.is_active:
            self._paper_om.simulate_fill(order.order_id, fill_price=fill_price)

        commission = _compute_commission(
            self._config.commission_mode,
            self._config.commission_value,
            fill_price,
            size,
        )
        self._cash -= commission

        self._position = direction
        self._entry_price = fill_price
        self._entry_time = ts
        self._entry_commission = commission
        self._size = size

        logger.debug(
            "OPEN %s: %d @ %.4f (commission=%.4f) ts=%s",
            direction,
            size,
            fill_price,
            commission,
            ts,
        )

    def _close_position(self, fill_price: float, ts: pd.Timestamp) -> None:
        """Close the current open position; record a completed trade.

        Args:
            fill_price: Actual fill price (after slippage).
            ts:         Trade timestamp.
        """
        size = self._size
        direction = self._position

        # Place closing order through PaperOrderManager
        close_side = (
            OrderSide.SELL.value if direction == "long" else OrderSide.BUY.value
        )
        order = self._paper_om.place_order(
            symbol="BT",
            side=close_side,
            quantity=size,
            order_type=OrderType.MARKET.value,
        )
        if order.is_active:
            order = self._paper_om.simulate_fill(order.order_id, fill_price)

        exit_commission = _compute_commission(
            self._config.commission_mode,
            self._config.commission_value,
            fill_price,
            size,
        )
        total_commission = self._entry_commission + exit_commission

        if direction == "long":
            gross_pnl = (fill_price - self._entry_price) * size * self._config.price_per_unit
        else:
            gross_pnl = (self._entry_price - fill_price) * size * self._config.price_per_unit

        net_pnl = gross_pnl - total_commission
        self._cash += net_pnl + self._entry_commission  # entry commission already debited

        trade_record = {
            "entry_time": self._entry_time,
            "exit_time": ts,
            "direction": direction,
            "size": size,
            "entry_price": self._entry_price,
            "exit_price": fill_price,
            "gross_pnl": gross_pnl,
            "commission": total_commission,
            "pnl": net_pnl,
        }
        self._trades.append(trade_record)

        logger.debug(
            "CLOSE %s: %d @ %.4f gross=%.4f net=%.4f ts=%s",
            direction,
            size,
            fill_price,
            gross_pnl,
            net_pnl,
            ts,
        )

        # Reset position state
        self._position = "flat"
        self._entry_price = 0.0
        self._entry_time = None
        self._entry_commission = 0.0
        self._size = 0.0

    def _mark_to_market(self, close_price: float) -> float:
        """Current equity = cash + unrealized P&L on open position.

        Args:
            close_price: Current bar close price.

        Returns:
            Mark-to-market equity value.
        """
        if self._position == "flat":
            return self._cash
        mult = self._config.price_per_unit
        if self._position == "long":
            unrealized = (close_price - self._entry_price) * self._size * mult
        else:
            unrealized = (self._entry_price - close_price) * self._size * mult
        return self._cash + unrealized

    # ------------------------------------------------------------------
    # Result assembly
    # ------------------------------------------------------------------

    def _build_result(self) -> BacktestResult:
        """Package run state into immutable BacktestResult."""
        equity = pd.Series(
            self._equity, index=self._ohlcv.index, name="equity"
        )
        returns = equity.pct_change().fillna(0.0)
        returns.name = "returns"

        trade_log = (
            pd.DataFrame(self._trades)
            if self._trades
            else pd.DataFrame(
                columns=[
                    "entry_time",
                    "exit_time",
                    "direction",
                    "size",
                    "entry_price",
                    "exit_price",
                    "gross_pnl",
                    "commission",
                    "pnl",
                ]
            )
        )

        metrics = PerformanceMetrics.calculate(
            returns, trade_count=len(self._trades)
        )

        orders = dict(self._paper_om._orders) if self._paper_om else {}

        return BacktestResult(
            equity_curve=equity,
            trade_log=trade_log,
            metrics=metrics,
            returns=returns,
            config=self._config,
            orders=orders,
        )
