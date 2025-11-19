"""Strategy backtesting primitives for the trading journal platform."""

from .engine import BacktestConfig, BacktestResult, run_backtest

__all__ = ["BacktestConfig", "BacktestResult", "run_backtest"]
