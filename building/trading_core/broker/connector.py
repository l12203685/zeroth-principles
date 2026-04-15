"""Broker connector module - Sinopac Shioaji API wrapper.

Merged from 17 instances of shioaji initialization across:
- sino-trade-api/function_file.py: get_api()
- AlgoTrading/backtest.py and other scripts
"""

from __future__ import annotations

import os
import json
import logging
from typing import Optional
from datetime import datetime, timedelta

try:
    import shioaji as sj  # type: ignore
except ImportError:  # pragma: no cover — optional dep
    # Defer the failure to the first real broker call so non-broker
    # modules (analytics, backtest, etc.) can import without shioaji.
    sj = None  # type: ignore

from trading_core.config import Settings, get_settings

logger = logging.getLogger(__name__)


class BrokerConnector:
    """Singleton wrapper for Shioaji API.

    Ensures only one API instance exists across the system.
    Handles login, CA certification, and connection management.
    """

    _instance: Optional["BrokerConnector"] = None
    _api: Optional["sj.Shioaji"] = None  # type: ignore[name-defined]

    def __new__(cls, settings: Optional[Settings] = None):
        """Singleton pattern - return same instance."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, settings: Optional[Settings] = None):
        """Initialize broker connector (only once per process).

        Args:
            settings: Settings instance. If None, uses global settings.

        Raises:
            ValueError: If API key or secret not provided in settings.
            ConnectionError: If login fails.
        """
        if self._initialized:
            return

        self.settings = settings or get_settings()
        self._api = None
        self._login_attempts = 0
        self._max_login_attempts = 3

        # Validate required settings
        if not self.settings.broker_api_key:
            raise ValueError("BROKER_API_KEY not set in environment")
        if not self.settings.broker_secret:
            raise ValueError("BROKER_SECRET not set in environment")

        self._initialized = True
        logger.info("BrokerConnector initialized")

    @property
    def api(self) -> sj.Shioaji:
        """Get or initialize API connection.

        Returns:
            Shioaji API instance

        Raises:
            ConnectionError: If login fails after max attempts.
        """
        if self._api is None:
            self._api = self._create_api()
        return self._api

    def _create_api(self) -> sj.Shioaji:
        """Create and login to Shioaji API.

        Returns:
            Authenticated Shioaji instance

        Raises:
            ConnectionError: If login fails.
        """
        if sj is None:
            raise ImportError(
                "shioaji package required for live broker. "
                "Install with: pip install shioaji"
            )
        logger.info("Creating new Shioaji API connection...")
        api = sj.Shioaji()

        try:
            # Prepare login credentials
            login_kwargs = {
                "api_key": self.settings.broker_api_key,
                "secret_key": self.settings.broker_secret,
                "contracts_cb": self._on_contracts_loaded,
            }

            # Login
            logger.debug("Logging in to Shioaji API...")
            accounts = api.login(**login_kwargs)
            logger.info(f"Login successful. Accounts: {accounts}")

            # Activate CA certification if path provided
            if self.settings.broker_ca_path and os.path.exists(
                self.settings.broker_ca_path
            ):
                self._activate_ca(api)
            elif self.settings.broker_ca_path:
                logger.warning(
                    f"CA certificate path not found: {self.settings.broker_ca_path}"
                )

            self._login_attempts = 0
            return api

        except Exception as e:
            self._login_attempts += 1
            logger.error(f"Login attempt {self._login_attempts} failed: {e}")

            if self._login_attempts >= self._max_login_attempts:
                raise ConnectionError(
                    f"Failed to login after {self._max_login_attempts} attempts"
                ) from e

            # Retry logic
            import time

            wait_time = 2 ** self._login_attempts  # exponential backoff
            logger.info(f"Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
            return self._create_api()

    def _activate_ca(self, api: sj.Shioaji) -> None:
        """Activate CA certification.

        Args:
            api: Shioaji API instance
        """
        try:
            logger.debug("Activating CA certification...")
            api.activate_ca(
                ca_path=self.settings.broker_ca_path,
                ca_passwd=self.settings.broker_person_id,
                person_id=self.settings.broker_person_id,
            )
            logger.info("CA certification activated successfully")
        except Exception as e:
            logger.warning(f"CA activation failed: {e}")

    @staticmethod
    def _on_contracts_loaded(contracts):
        """Callback when contracts are loaded from API.

        Args:
            contracts: Contracts loaded from API
        """
        logger.debug(f"Contracts loaded: {len(list(contracts)) if contracts else 0}")

    def get_account_margin(self) -> dict:
        """Get account margin information.

        Returns:
            Account margin data
        """
        margin = self.api.get_account_margin()
        return margin.data() if hasattr(margin, "data") else margin

    def get_open_positions(self, product_type: str = "0") -> dict:
        """Get account open positions.

        Args:
            product_type: '0' for futures, '1' for options

        Returns:
            Open positions data
        """
        positions = self.api.get_account_openposition(
            product_type=product_type, query_type="1", account=self.api.futopt_account
        )
        return positions.data() if hasattr(positions, "data") else positions

    def get_near_month_future_contract(self, code: str = "TXF"):
        """Get near month future contract.

        Merged from sino-trade-api/function_file.py: get_near_month_future_contract()

        Args:
            code: Contract code (default 'TXF')

        Returns:
            Contract object
        """
        now = datetime.now()
        change_month_time = datetime(now.year, now.month, 14, 13, 30) + timedelta(
            days=datetime(now.year, now.month, 15).isoweekday() + 3
        )

        if now <= change_month_time:
            contract_code = code + now.strftime("%Y%m")
        else:
            next_month = now.month + 1
            next_year = now.year
            if next_month == 13:
                next_month = 1
                next_year += 1
            contract_code = code + f"{next_year}{next_month:02d}"

        try:
            return self.api.Contracts.Futures[code][contract_code]
        except KeyError:
            logger.error(f"Contract not found: {contract_code}")
            raise

    def get_near_week_future_contract(self, code: str = "MX"):
        """Get near week future contract.

        Merged from sino-trade-api/function_file.py: get_near_week_future_contract()

        Args:
            code: Contract code (default 'MX' for micro contracts)

        Returns:
            Contract object
        """
        now = datetime.now()
        week_maturity = self._get_near_week_maturity(now)

        week_num = (week_maturity.day + 6) // 7  # 1-4 for week, 5->F for monthly
        week_code = str(week_num).replace("5", "F")
        contract_code = code + week_code + week_maturity.strftime("%Y%m")

        try:
            return self.api.Contracts.Futures[code][contract_code]
        except KeyError:
            logger.error(f"Contract not found: {contract_code}")
            raise

    @staticmethod
    def _get_near_week_maturity(now: Optional[datetime] = None) -> datetime:
        """Get near week maturity date.

        Args:
            now: Current datetime (default now)

        Returns:
            Maturity datetime
        """
        if now is None:
            now = datetime.now()

        change_week_time = (
            datetime(now.year, now.month, now.day, 13, 30)
            + timedelta(days=3)
            - timedelta(days=datetime(now.year, now.month, now.day).isoweekday() - 1)
        )

        if now > change_week_time:
            now += timedelta(days=7)

        return (
            datetime(now.year, now.month, now.day, 13, 30)
            + timedelta(days=3)
            - timedelta(days=datetime(now.year, now.month, now.day).isoweekday() - 1)
        )

    def logout(self) -> None:
        """Logout from API."""
        if self._api is not None:
            try:
                self._api.logout()
                logger.info("Logged out from API")
            except Exception as e:
                logger.error(f"Logout failed: {e}")
            finally:
                self._api = None

    def reset(self) -> None:
        """Reset singleton instance (for testing)."""
        self.logout()
        BrokerConnector._instance = None
        BrokerConnector._api = None


def get_api(settings: Optional[Settings] = None) -> sj.Shioaji:
    """Get Shioaji API instance (singleton).

    Convenience function to get the API from global BrokerConnector.

    Args:
        settings: Settings instance (optional)

    Returns:
        Shioaji API instance
    """
    connector = BrokerConnector(settings)
    return connector.api
