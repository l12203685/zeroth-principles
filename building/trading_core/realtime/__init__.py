"""Realtime trading engine module.

Provides the RealtimeEngine class for live trading with:
- Market session awareness (TW futures day/night sessions)
- Auto-reconnect with exponential backoff
- Heartbeat / health monitoring
- Signal → Order pipeline with risk checks
- Position tracking
- Graceful shutdown
- Event-driven callbacks: on_tick, on_bar, on_fill, on_error
"""

from trading_core.realtime.engine import (
    RealtimeEngine,
    EngineState,
    MarketSession,
    TradingSignal,
    SignalAction,
    EngineConfig,
    RiskLimits,
    HealthStatus,
)

__all__ = [
    "RealtimeEngine",
    "EngineState",
    "MarketSession",
    "TradingSignal",
    "SignalAction",
    "EngineConfig",
    "RiskLimits",
    "HealthStatus",
]
