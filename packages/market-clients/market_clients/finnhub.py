from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import requests


@dataclass(slots=True)
class FinnhubClient:
    api_key: str
    base_url: str = "https://finnhub.io/api/v1"

    def quote(self, symbol: str) -> dict[str, Any]:
        resp = requests.get(
            f"{self.base_url}/quote",
            params={"symbol": symbol, "token": self.api_key},
            timeout=10,
        )
        resp.raise_for_status()
        return resp.json()
