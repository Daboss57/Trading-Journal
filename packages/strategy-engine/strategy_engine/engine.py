from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(slots=True)
class BacktestConfig:
    symbol: str
    cash: float
    strategy: str


@dataclass(slots=True)
class BacktestResult:
    symbol: str
    strategy: str
    trades: int
    net_return_pct: float


def run_backtest(config: BacktestConfig, prices: Iterable[float]) -> BacktestResult:
    """Placeholder implementation used for scaffolding CI."""

    prices = list(prices)
    if not prices:
        raise ValueError("Price series cannot be empty")

    pct_change = (prices[-1] - prices[0]) / prices[0]
    return BacktestResult(
        symbol=config.symbol,
        strategy=config.strategy,
        trades=len(prices) // 5,
        net_return_pct=round(pct_change * 100, 4),
    )
