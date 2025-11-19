from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import requests


@dataclass(slots=True)
class AlphaVantageClient:
    api_key: str
    base_url: str = "https://www.alphavantage.co/query"

    def intraday(self, symbol: str, interval: str = "5min") -> dict[str, Any]:
        resp = requests.get(
            self.base_url,
            params={
                "function": "TIME_SERIES_INTRADAY",
                "symbol": symbol,
                "interval": interval,
                "apikey": self.api_key,
            },
            timeout=20,
        )
        resp.raise_for_status()
        return resp.json()
