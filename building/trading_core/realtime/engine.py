"""Realtime trading engine for TW futures.

Manages the full lifecycle of live trading:
- Market session awareness  (day 08:45-13:45, night 15:00-05:00)
- Auto-reconnect with exponential backoff
- Heartbeat / health monitoring
- Signal → validation → Order pipeline
- Position tracking and risk checks
- Graceful shutdown (cancel pending → optional flatten)
- Event-driven callbacks: on_tick, on_bar, on_fill, on_error
"""

from __future__ import annotations

import logging
import threading
import time
from dataclasses import dataclass, field
from datetime import datetime, time as dtime, timedelta
from enum import Enum, auto
from typing import Callable, Dict, List, Optional

from trading_core.broker.orders import (
    AbstractOrderManager,
    Order,
    OrderSide,
    OrderStatus,
    OrderType,
)
from trading_core.data.positions import Portfolio, Position, PositionType

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Enumerations
# ---------------------------------------------------------------------------


class EngineState(Enum):
    """Lifecycle states of the realtime engine."""

    IDLE = auto()           # Not started
    CONNECTING = auto()     # Establishing broker connection
    WAITING = auto()        # Connected but outside market hours
    RUNNING = auto()        # Inside market session, processing events
    RECONNECTING = auto()   # Lost connection, backing off before retry
    STOPPING = auto()       # Graceful shutdown in progress
    STOPPED = auto()        # Fully stopped


class MarketSession(Enum):
    """TW futures market sessions."""

    CLOSED = "closed"
    DAY = "day"      # 08:45 – 13:45 (local TW time)
    NIGHT = "night"  # 15:00 – next day 05:00 (local TW time)


class SignalAction(Enum):
    """Trading signal actions."""

    BUY = "BUY"
    SELL = "SELL"
    FLAT = "FLAT"   # Close / flatten position


# ---------------------------------------------------------------------------
# Data transfer objects
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class TradingSignal:
    """Immutable trading signal produced by a strategy.

    Attributes:
        symbol:     Instrument symbol (e.g. "TXF").
        action:     BUY, SELL, or FLAT.
        quantity:   Number of contracts (> 0).
        order_type: "MARKET" or "LIMIT".
        price:      Limit price (required when order_type == "LIMIT").
        source:     Identifier of the strategy/indicator that generated this signal.
        timestamp:  When the signal was generated.
    """

    symbol: str
    action: SignalAction
    quantity: float
    order_type: str = "MARKET"
    price: Optional[float] = None
    source: str = "unknown"
    timestamp: datetime = field(default_factory=datetime.now)

    def __post_init__(self) -> None:
        if self.quantity <= 0:
            raise ValueError(f"Signal quantity must be positive, got {self.quantity}")
        if self.order_type.upper() == "LIMIT" and self.price is None:
            raise ValueError("LIMIT signals require a price")


@dataclass
class RiskLimits:
    """Risk parameters applied before each order.

    Attributes:
        max_position_size:  Maximum absolute position in contracts.
        max_order_size:     Maximum single-order quantity.
        max_daily_loss:     Maximum realised loss for the day (absolute value,
                            e.g. 50_000 = stop trading at -50,000 PnL).
        max_drawdown_pct:   Maximum drawdown from peak equity (0.0–1.0).
                            Set to 1.0 to disable.
        flatten_on_shutdown: If True, the engine closes all positions during
                            graceful shutdown.
    """

    max_position_size: float = 10.0
    max_order_size: float = 5.0
    max_daily_loss: float = 100_000.0
    max_drawdown_pct: float = 0.20
    flatten_on_shutdown: bool = False


@dataclass
class EngineConfig:
    """Engine configuration.

    Attributes:
        heartbeat_interval: Seconds between heartbeat checks.
        reconnect_max_attempts: 0 means retry indefinitely.
        reconnect_base_delay: Initial backoff delay in seconds.
        reconnect_max_delay: Maximum backoff delay in seconds.
        poll_interval: Seconds between market-hours-check ticks while WAITING.
        timezone_offset_hours: Local time = UTC + offset (TW = +8).
    """

    heartbeat_interval: float = 30.0
    reconnect_max_attempts: int = 0           # 0 = infinite
    reconnect_base_delay: float = 2.0
    reconnect_max_delay: float = 120.0
    poll_interval: float = 10.0
    timezone_offset_hours: int = 8


@dataclass
class HealthStatus:
    """Snapshot of engine health.

    Attributes:
        state:            Current EngineState.
        session:          Current MarketSession.
        last_heartbeat:   When the last heartbeat completed.
        reconnect_count:  Total reconnection attempts so far.
        active_orders:    Number of currently active orders.
        open_positions:   Number of open positions.
        daily_pnl:        Unrealised + realised PnL for today.
        is_healthy:       True if the engine is RUNNING and the heartbeat is recent.
    """

    state: EngineState
    session: MarketSession
    last_heartbeat: Optional[datetime]
    reconnect_count: int
    active_orders: int
    open_positions: int
    daily_pnl: float
    is_healthy: bool


# ---------------------------------------------------------------------------
# Market session helpers
# ---------------------------------------------------------------------------


# TW futures session boundaries (local time)
_DAY_START = dtime(8, 45)
_DAY_END = dtime(13, 45)
_NIGHT_START = dtime(15, 0)
_NIGHT_END = dtime(5, 0)   # next calendar day


def get_market_session(now: Optional[datetime] = None) -> MarketSession:
    """Determine the current TW futures market session.

    TW futures sessions (local Taipei time, UTC+8):
    - Day session:   08:45 – 13:45
    - Night session: 15:00 – (next day) 05:00
    - Closed: all other times

    Args:
        now: Datetime to evaluate (defaults to current local time).

    Returns:
        MarketSession enum value.
    """
    if now is None:
        now = datetime.now()

    t = now.time()

    # Day session
    if _DAY_START <= t <= _DAY_END:
        return MarketSession.DAY

    # Night session spans midnight:
    #   15:00 – 23:59:59  → night
    #   00:00 – 05:00     → night
    if t >= _NIGHT_START or t <= _NIGHT_END:
        return MarketSession.NIGHT

    return MarketSession.CLOSED


def next_session_open(now: Optional[datetime] = None) -> datetime:
    """Return the datetime of the next session open after *now*.

    Args:
        now: Reference time (defaults to current local time).

    Returns:
        Datetime of the next session open.
    """
    if now is None:
        now = datetime.now()

    current_session = get_market_session(now)

    today_date = now.date()

    if current_session == MarketSession.CLOSED:
        t = now.time()
        # Between night close (05:00) and day open (08:45)
        if _NIGHT_END < t < _DAY_START:
            return datetime.combine(today_date, _DAY_START)
        # Between day close (13:45) and night open (15:00)
        if _DAY_END < t < _NIGHT_START:
            return datetime.combine(today_date, _NIGHT_START)

    if current_session == MarketSession.DAY:
        return datetime.combine(today_date, _NIGHT_START)

    if current_session == MarketSession.NIGHT:
        # Night session opens today and next day open is tomorrow's day session
        tomorrow = today_date + timedelta(days=1)
        return datetime.combine(tomorrow, _DAY_START)

    # Fallback
    return datetime.combine(today_date, _DAY_START)


# ---------------------------------------------------------------------------
# RealtimeEngine
# ---------------------------------------------------------------------------


class RealtimeEngine:
    """Event-driven realtime trading engine for TW futures.

    Usage::

        def on_fill(order: Order, engine: RealtimeEngine) -> None:
            logger.info("Filled: %s", order.order_id)

        engine = RealtimeEngine(order_manager=PaperOrderManager(), on_fill=on_fill)
        engine.start()
        engine.submit_signal(TradingSignal("TXF", SignalAction.BUY, 1))
        engine.stop()

    Args:
        order_manager:  Concrete AbstractOrderManager for order submission.
        portfolio:      Portfolio instance for position tracking.
        risk:           RiskLimits configuration.
        config:         EngineConfig for tuning behaviour.
        on_tick:        Callback invoked on each tick dict received.
        on_bar:         Callback invoked on each completed OHLCV bar dict.
        on_fill:        Callback invoked when an order is filled.
        on_error:       Callback invoked on non-fatal engine errors.
        connect_fn:     Optional callable executed to (re)establish the broker
                        connection. Use for live broker login; omit for paper trading.
        disconnect_fn:  Optional callable executed to cleanly disconnect.
    """

    def __init__(
        self,
        order_manager: AbstractOrderManager,
        portfolio: Optional[Portfolio] = None,
        risk: Optional[RiskLimits] = None,
        config: Optional[EngineConfig] = None,
        on_tick: Optional[Callable[[Dict], None]] = None,
        on_bar: Optional[Callable[[Dict], None]] = None,
        on_fill: Optional[Callable[[Order, "RealtimeEngine"], None]] = None,
        on_error: Optional[Callable[[Exception, "RealtimeEngine"], None]] = None,
        connect_fn: Optional[Callable[[], None]] = None,
        disconnect_fn: Optional[Callable[[], None]] = None,
    ) -> None:
        self._order_manager = order_manager
        self._portfolio = portfolio or Portfolio()
        self._risk = risk or RiskLimits()
        self._config = config or EngineConfig()

        # Event callbacks
        self._on_tick = on_tick
        self._on_bar = on_bar
        self._on_fill = on_fill
        self._on_error = on_error

        # Connection hooks
        self._connect_fn = connect_fn
        self._disconnect_fn = disconnect_fn

        # State
        self._state: EngineState = EngineState.IDLE
        self._state_lock = threading.Lock()
        self._stop_event = threading.Event()

        # Heartbeat tracking
        self._last_heartbeat: Optional[datetime] = None
        self._heartbeat_thread: Optional[threading.Thread] = None

        # Reconnect tracking
        self._reconnect_count: int = 0
        self._reconnect_attempt: int = 0

        # Daily P&L tracking
        self._daily_pnl: float = 0.0
        self._peak_equity: float = self._portfolio.total_value

        logger.info("RealtimeEngine initialised")

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    @property
    def state(self) -> EngineState:
        """Current engine state (thread-safe read)."""
        with self._state_lock:
            return self._state

    def start(self) -> None:
        """Start the engine in a background thread.

        Transitions: IDLE → CONNECTING → WAITING / RUNNING

        Raises:
            RuntimeError: If the engine is not in IDLE or STOPPED state.
        """
        with self._state_lock:
            if self._state not in (EngineState.IDLE, EngineState.STOPPED):
                raise RuntimeError(
                    f"Cannot start engine from state {self._state}"
                )
            self._state = EngineState.CONNECTING
            self._stop_event.clear()

        self._main_thread = threading.Thread(
            target=self._run_loop, daemon=True, name="rtengine-main"
        )
        self._main_thread.start()
        logger.info("RealtimeEngine started")

    def stop(self, timeout: float = 15.0) -> None:
        """Gracefully stop the engine.

        - Cancels all pending orders.
        - If risk.flatten_on_shutdown is True, submits market orders to close
          all open positions.
        - Disconnects from the broker.
        - Waits up to *timeout* seconds for the background thread to exit.

        Args:
            timeout: Maximum seconds to wait for the background thread.
        """
        logger.info("RealtimeEngine stop requested")
        with self._state_lock:
            if self._state in (EngineState.STOPPED, EngineState.STOPPING):
                return
            self._state = EngineState.STOPPING

        self._stop_event.set()

        # Graceful cleanup (runs in calling thread for predictability)
        try:
            self._cancel_all_pending_orders()
            if self._risk.flatten_on_shutdown:
                self._flatten_all_positions()
            self._disconnect()
        except Exception as exc:
            logger.error("Error during shutdown cleanup: %s", exc)
            self._fire_error(exc)

        # Wait for background thread
        if hasattr(self, "_main_thread") and self._main_thread.is_alive():
            self._main_thread.join(timeout=timeout)

        with self._state_lock:
            self._state = EngineState.STOPPED

        logger.info("RealtimeEngine stopped")

    def submit_signal(self, signal: TradingSignal) -> Optional[Order]:
        """Process a trading signal through validation and order submission.

        The pipeline:
        1. Validate signal schema (already enforced by TradingSignal.__post_init__).
        2. Check engine state (must be RUNNING or WAITING).
        3. Check market session (must be open to trade).
        4. Apply risk limits.
        5. Submit order via AbstractOrderManager.

        Args:
            signal: TradingSignal to process.

        Returns:
            Submitted Order if successful, None if rejected by risk or state checks.
        """
        logger.info(
            "Signal received: %s %s %s x%s from %s",
            signal.action.value,
            signal.symbol,
            signal.order_type,
            signal.quantity,
            signal.source,
        )

        # State check
        if self.state not in (EngineState.RUNNING, EngineState.WAITING):
            logger.warning("Signal rejected: engine not running (state=%s)", self.state)
            return None

        # Session check
        session = get_market_session()
        if session == MarketSession.CLOSED:
            logger.warning("Signal rejected: market is closed")
            return None

        # Risk checks
        rejection = self._check_risk(signal)
        if rejection:
            logger.warning("Signal rejected by risk: %s", rejection)
            return None

        # FLAT action → cancel all then close position
        if signal.action == SignalAction.FLAT:
            return self._handle_flat_signal(signal)

        # BUY / SELL → place order
        side = OrderSide.BUY if signal.action == SignalAction.BUY else OrderSide.SELL
        try:
            order = self._order_manager.place_order(
                symbol=signal.symbol,
                side=side.value,
                quantity=signal.quantity,
                order_type=signal.order_type.upper(),
                price=signal.price,
            )
            logger.info("Order submitted: %s", order.order_id)
            # If the broker immediately fills the order (e.g. paper trading),
            # process the fill now so the portfolio stays in sync.
            if order.status in (OrderStatus.FILLED, OrderStatus.PARTIAL):
                self.on_fill(order)
            return order
        except Exception as exc:
            logger.error("Order submission failed: %s", exc)
            self._fire_error(exc)
            return None

    def on_tick(self, tick: Dict) -> None:
        """Dispatch a tick event to the registered callback.

        Call this from your data feed / broker subscription handler.

        Args:
            tick: Tick data dict with at minimum {"symbol": str, "price": float}.
        """
        # Update portfolio prices
        symbol = tick.get("symbol")
        price = tick.get("price")
        if symbol and price is not None:
            self._portfolio.update_prices({symbol: price})
            self._update_daily_pnl()

        if self._on_tick is not None:
            try:
                self._on_tick(tick)
            except Exception as exc:
                logger.error("on_tick callback error: %s", exc)
                self._fire_error(exc)

    def on_bar(self, bar: Dict) -> None:
        """Dispatch a completed bar event to the registered callback.

        Args:
            bar: OHLCV bar dict with keys open, high, low, close, volume, symbol.
        """
        if self._on_bar is not None:
            try:
                self._on_bar(bar)
            except Exception as exc:
                logger.error("on_bar callback error: %s", exc)
                self._fire_error(exc)

    def on_fill(self, order: Order) -> None:
        """Notify the engine that an order has been filled.

        Updates the portfolio position and fires the on_fill callback.

        Args:
            order: Filled Order object.
        """
        logger.info(
            "Fill: %s %s x%.0f @ %.2f",
            order.side.value,
            order.symbol,
            order.filled_quantity,
            order.avg_fill_price or 0.0,
        )

        # Update portfolio based on fill
        self._apply_fill_to_portfolio(order)
        self._update_daily_pnl()

        if self._on_fill is not None:
            try:
                self._on_fill(order, self)
            except Exception as exc:
                logger.error("on_fill callback error: %s", exc)
                self._fire_error(exc)

    def health(self) -> HealthStatus:
        """Return a snapshot of the engine's health.

        Returns:
            HealthStatus with current metrics.
        """
        active_orders = len(self._order_manager.list_active_orders())
        open_positions = len(
            [p for p in self._portfolio.positions.values() if p.is_open]
        )
        now = datetime.now()
        heartbeat_ok = (
            self._last_heartbeat is not None
            and (now - self._last_heartbeat).total_seconds()
            < self._config.heartbeat_interval * 3
        )
        return HealthStatus(
            state=self.state,
            session=get_market_session(now),
            last_heartbeat=self._last_heartbeat,
            reconnect_count=self._reconnect_count,
            active_orders=active_orders,
            open_positions=open_positions,
            daily_pnl=self._daily_pnl,
            is_healthy=self.state == EngineState.RUNNING and heartbeat_ok,
        )

    # ------------------------------------------------------------------
    # Internal main loop
    # ------------------------------------------------------------------

    def _run_loop(self) -> None:
        """Main engine loop: connect → wait for market → run → reconnect on error."""
        self._reconnect_attempt = 0

        while not self._stop_event.is_set():
            try:
                self._connect()
                self._set_state(EngineState.WAITING)
                self._wait_for_market()
                if self._stop_event.is_set():
                    break
                self._set_state(EngineState.RUNNING)
                self._start_heartbeat()
                self._market_loop()

            except Exception as exc:
                logger.error("Engine loop error: %s", exc)
                self._fire_error(exc)

                if self._stop_event.is_set():
                    break

                should_retry = self._handle_reconnect()
                if not should_retry:
                    logger.error("Max reconnect attempts reached. Stopping engine.")
                    break

        with self._state_lock:
            if self._state not in (EngineState.STOPPING, EngineState.STOPPED):
                self._state = EngineState.STOPPED
        logger.info("Engine loop exited")

    def _connect(self) -> None:
        """Establish the broker connection."""
        self._set_state(EngineState.CONNECTING)
        if self._connect_fn is not None:
            logger.info("Connecting to broker...")
            self._connect_fn()
        logger.info("Broker connection established")

    def _disconnect(self) -> None:
        """Tear down the broker connection."""
        if self._disconnect_fn is not None:
            try:
                self._disconnect_fn()
            except Exception as exc:
                logger.error("Disconnect error: %s", exc)

    def _wait_for_market(self) -> None:
        """Block until the market session opens (or stop is requested)."""
        session = get_market_session()
        if session != MarketSession.CLOSED:
            return

        next_open = next_session_open()
        wait_seconds = (next_open - datetime.now()).total_seconds()
        if wait_seconds > 0:
            logger.info(
                "Market closed. Next session opens at %s (in %.0f s)",
                next_open.strftime("%H:%M"),
                wait_seconds,
            )

        while not self._stop_event.is_set():
            if get_market_session() != MarketSession.CLOSED:
                return
            self._stop_event.wait(timeout=self._config.poll_interval)

    def _market_loop(self) -> None:
        """Spin while the market is open. Exits when market closes or stop is requested."""
        logger.info("Market session open. Engine RUNNING.")
        while not self._stop_event.is_set():
            session = get_market_session()
            if session == MarketSession.CLOSED:
                logger.info("Market closed. Transitioning to WAITING.")
                self._set_state(EngineState.WAITING)
                return
            self._stop_event.wait(timeout=self._config.poll_interval)

    # ------------------------------------------------------------------
    # Heartbeat
    # ------------------------------------------------------------------

    def _start_heartbeat(self) -> None:
        """Launch the heartbeat thread (daemon)."""
        if self._heartbeat_thread and self._heartbeat_thread.is_alive():
            return

        self._heartbeat_thread = threading.Thread(
            target=self._heartbeat_loop, daemon=True, name="rtengine-heartbeat"
        )
        self._heartbeat_thread.start()

    def _heartbeat_loop(self) -> None:
        """Periodically log engine health metrics."""
        while not self._stop_event.is_set():
            self._stop_event.wait(timeout=self._config.heartbeat_interval)
            if self._stop_event.is_set():
                break

            self._last_heartbeat = datetime.now()
            h = self.health()
            logger.info(
                "[HEARTBEAT] state=%s session=%s orders=%d positions=%d pnl=%.0f",
                h.state.name,
                h.session.value,
                h.active_orders,
                h.open_positions,
                h.daily_pnl,
            )

    # ------------------------------------------------------------------
    # Reconnect logic
    # ------------------------------------------------------------------

    def _handle_reconnect(self) -> bool:
        """Back off and decide whether to retry.

        Returns:
            True  → caller should retry the connection loop.
            False → max attempts exceeded; caller should stop.
        """
        max_attempts = self._config.reconnect_max_attempts
        if max_attempts != 0 and self._reconnect_attempt >= max_attempts:
            return False

        self._reconnect_attempt += 1
        self._reconnect_count += 1
        self._set_state(EngineState.RECONNECTING)

        delay = min(
            self._config.reconnect_base_delay * (2 ** (self._reconnect_attempt - 1)),
            self._config.reconnect_max_delay,
        )
        logger.info(
            "Reconnect attempt %d (delay=%.1fs)", self._reconnect_attempt, delay
        )
        self._stop_event.wait(timeout=delay)
        return not self._stop_event.is_set()

    # ------------------------------------------------------------------
    # Risk
    # ------------------------------------------------------------------

    def _check_risk(self, signal: TradingSignal) -> Optional[str]:
        """Apply risk limits to a signal.

        Args:
            signal: The candidate signal.

        Returns:
            Rejection reason string, or None if signal passes all checks.
        """
        # Order size
        if signal.quantity > self._risk.max_order_size:
            return (
                f"order size {signal.quantity} > max_order_size {self._risk.max_order_size}"
            )

        # Position size after fill
        current_pos_size = self._current_position_size(signal.symbol)
        if signal.action == SignalAction.BUY:
            projected = current_pos_size + signal.quantity
        elif signal.action == SignalAction.SELL:
            projected = current_pos_size - signal.quantity
        else:
            projected = 0.0  # FLAT

        if abs(projected) > self._risk.max_position_size:
            return (
                f"projected position {projected:.0f} exceeds "
                f"max_position_size {self._risk.max_position_size}"
            )

        # Daily loss
        if self._daily_pnl < -abs(self._risk.max_daily_loss):
            return (
                f"daily PnL {self._daily_pnl:.0f} exceeds "
                f"max_daily_loss {self._risk.max_daily_loss}"
            )

        # Drawdown
        equity = self._portfolio.total_value
        if equity > self._peak_equity:
            self._peak_equity = equity

        if self._peak_equity > 0:
            drawdown = (self._peak_equity - equity) / self._peak_equity
            if drawdown > self._risk.max_drawdown_pct:
                return (
                    f"drawdown {drawdown:.1%} exceeds "
                    f"max_drawdown_pct {self._risk.max_drawdown_pct:.1%}"
                )

        return None

    def _current_position_size(self, symbol: str) -> float:
        """Net signed position size for *symbol* in the portfolio.

        Positive = long, negative = short.
        """
        pos = self._portfolio.get_position(symbol)
        if pos is None or not pos.is_open:
            return 0.0
        return pos.size * pos.direction.value

    # ------------------------------------------------------------------
    # Order helpers
    # ------------------------------------------------------------------

    def _handle_flat_signal(self, signal: TradingSignal) -> Optional[Order]:
        """Cancel all pending orders and close the open position for *symbol*."""
        self._cancel_symbol_orders(signal.symbol)

        pos = self._portfolio.get_position(signal.symbol)
        if pos is None or not pos.is_open:
            logger.info("FLAT: no open position for %s", signal.symbol)
            return None

        # Close by sending opposite market order
        close_side = (
            OrderSide.SELL
            if pos.direction == PositionType.LONG
            else OrderSide.BUY
        )
        try:
            order = self._order_manager.place_order(
                symbol=signal.symbol,
                side=close_side.value,
                quantity=pos.size,
                order_type="MARKET",
            )
            logger.info("FLAT order submitted: %s", order.order_id)
            # Process immediate fills (paper trading, etc.)
            if order.status in (OrderStatus.FILLED, OrderStatus.PARTIAL):
                self.on_fill(order)
            return order
        except Exception as exc:
            logger.error("FLAT order failed: %s", exc)
            self._fire_error(exc)
            return None

    def _cancel_all_pending_orders(self) -> None:
        """Cancel every active (PENDING/PARTIAL) order."""
        active = self._order_manager.list_active_orders()
        for order in active:
            try:
                self._order_manager.cancel_order(order.order_id)
                logger.info("Cancelled order %s", order.order_id)
            except Exception as exc:
                logger.warning("Could not cancel %s: %s", order.order_id, exc)

    def _cancel_symbol_orders(self, symbol: str) -> None:
        """Cancel all active orders for a specific symbol."""
        active = self._order_manager.list_active_orders()
        for order in active:
            if order.symbol == symbol.upper():
                try:
                    self._order_manager.cancel_order(order.order_id)
                except Exception as exc:
                    logger.warning("Could not cancel %s: %s", order.order_id, exc)

    def _flatten_all_positions(self) -> None:
        """Submit market orders to close every open position."""
        for symbol, pos in list(self._portfolio.positions.items()):
            if not pos.is_open:
                continue
            signal = TradingSignal(
                symbol=symbol,
                action=SignalAction.FLAT,
                quantity=pos.size,
            )
            self._handle_flat_signal(signal)

    # ------------------------------------------------------------------
    # Portfolio / PnL helpers
    # ------------------------------------------------------------------

    def _apply_fill_to_portfolio(self, order: Order) -> None:
        """Update portfolio based on a filled order.

        Args:
            order: A filled Order with avg_fill_price set.
        """
        if order.status not in (OrderStatus.FILLED, OrderStatus.PARTIAL):
            return
        if order.avg_fill_price is None:
            return

        direction = "long" if order.side == OrderSide.BUY else "short"
        qty = order.filled_quantity
        price = order.avg_fill_price

        existing = self._portfolio.get_position(order.symbol)
        if existing and existing.is_open:
            # Opposite side → close / reduce
            existing_dir = (
                PositionType.LONG
                if existing.direction == PositionType.LONG
                else PositionType.SHORT
            )
            closing = (
                order.side == OrderSide.SELL and existing_dir == PositionType.LONG
            ) or (
                order.side == OrderSide.BUY and existing_dir == PositionType.SHORT
            )
            if closing:
                if qty >= existing.size:
                    self._portfolio.close_position(order.symbol, price)
                else:
                    # Partial close → update size
                    new_size = existing.size - qty
                    self._portfolio.add_position(
                        symbol=order.symbol,
                        direction=existing.direction.name.lower(),
                        size=new_size,
                        entry_price=existing.entry_price,
                    )
                return

        # Open or add to position
        self._portfolio.add_position(
            symbol=order.symbol,
            direction=direction,
            size=qty,
            entry_price=price,
        )

    def _update_daily_pnl(self) -> None:
        """Refresh _daily_pnl from the portfolio's unrealised P&L."""
        self._daily_pnl = self._portfolio.portfolio_pnl

    # ------------------------------------------------------------------
    # Utility
    # ------------------------------------------------------------------

    def _set_state(self, new_state: EngineState) -> None:
        with self._state_lock:
            old = self._state
            self._state = new_state
        if old != new_state:
            logger.info("Engine state: %s → %s", old.name, new_state.name)

    def _fire_error(self, exc: Exception) -> None:
        """Invoke the on_error callback if registered."""
        if self._on_error is not None:
            try:
                self._on_error(exc, self)
            except Exception:  # noqa: BLE001
                pass
