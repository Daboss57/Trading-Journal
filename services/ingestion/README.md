# Ingestion Service

Bridges external market data providers into our internal caches (Redis, Blob Storage, TimescaleDB).

## Responsibilities
- Maintain long-lived WebSocket sessions for Finnhub (equities + crypto).
- Schedule Alpha Vantage + yfinance polls with built-in rate limiting.
- Publish normalized ticks into Redis Streams and durable storage.

## Current Status
- `pyproject.toml` wired to `market-clients`, `redis`, `pandas`, `pyarrow`, and `websockets`.
- `ingestion.main` exposes `ingestion-finnhub-ws` console script.
- `FinnhubStream` connects to `wss://ws.finnhub.io`, subscribes to configured symbols, logs throughput, snapshots via REST, pushes trades into Redis Streams, and writes Parquet batches under `storage/parquet/`.

## Local Run
```powershell
cd services/ingestion
uv sync
$env:FINNHUB_API_KEY="..."
$env:REDIS_URL="redis://localhost:6379/0"
uv run ingestion-finnhub-ws --duration 15 --symbols BINANCE:BTCUSDT TSLA
```

Requires `FINNHUB_API_KEY` and `REDIS_URL` in your environment (or `.env`).
