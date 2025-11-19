"""Market data ingestion entry points."""

from .finnhub_ws import FinnhubStream

__all__ = ["FinnhubStream"]
