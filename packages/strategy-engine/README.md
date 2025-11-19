# strategy-engine

Shared Python package for deterministic, vectorized backtesting routines.

## Usage

```python
from strategy_engine import BacktestConfig, run_backtest

config = BacktestConfig(symbol="TSLA", cash=10_000, strategy="buy-hold")
print(run_backtest(config, [10, 12, 13, 15, 14]))
```

## Roadmap
- Port notebook prototypes into typed pandas/numba routines.
- Add position sizing utilities + slippage modeling.
- Publish as internal package via GitHub Packages or Azure Artifacts.
