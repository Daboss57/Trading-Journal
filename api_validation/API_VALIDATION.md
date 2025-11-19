# API Validation Report (Initial Pass)

Date: 2025-11-18
Status: Active validation (Alpha Vantage, CoinGecko, yfinance, Finnhub verified)

## Scope
Validate accessibility, rate limits, and sample data retrieval for:
- Finnhub (real-time quotes/WebSocket) — key set via `FINNHUB_API_KEY`
- Alpha Vantage (historical & some intraday) — production key supplied
- Yahoo Finance via `yfinance` (historical OHLC) — no key
- CoinGecko (crypto pricing) — no key

## Environment Assumptions
Windows PowerShell 5.1, Python environment to be configured. Keys to be injected via environment variables:
- `FINNHUB_API_KEY`
- `ALPHAVANTAGE_API_KEY` (optional if not using demo)

## Finnhub
- REST Endpoint: `https://finnhub.io/api/v1/quote?symbol=TSLA&token=$env:FINNHUB_API_KEY`
	- Command: `Invoke-RestMethod` (PowerShell) after exporting provided key to `$env:FINNHUB_API_KEY`.
	- Response Snapshot: `{ "c": 401.25, "d": -7.67, "dp": -1.8757, "h": 408.9, "l": 393.71, "o": 405.38, "pc": 408.92, "t": 1763499600 }` (values reflect last quote; `t` in epoch seconds).
- WebSocket Endpoint: `wss://ws.finnhub.io?token=$env:FINNHUB_API_KEY`
	- Script: `api_validation/finnhub_ws_test.py` (uses `websockets` lib) subscribes to `TSLA`, `SPY`, and `BINANCE:BTCUSDT` to ensure live ticks even when equities are closed.
	- Output Sample (12s run): multiple `trade` payloads with BTCUSDT prices around `92,693` and volumes down to `6e-5`, confirming streaming functionality; equities idle after hours as expected.
- Rate Limit: ~60 REST calls/min (free tier) plus real-time WebSocket stream. Plan for batching quote requests + reconnect logic (ping interval 15s, jittered re-subscribe) in production.

## Alpha Vantage
- Endpoint Hit: `https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=P8LKSOV82NK25625`
- Command: `Invoke-RestMethod` (PowerShell) + selective projection of metadata + first 3 timestamps.
- Response Excerpt:
	```json
	{
		"Meta Data": {
			"1. Information": "Intraday (5min) open, high, low, close prices and volume",
			"2. Symbol": "IBM",
			"3. Last Refreshed": "2025-11-18 19:55:00",
			"4. Interval": "5min",
			"5. Output Size": "Compact",
			"6. Time Zone": "US/Eastern"
		},
		"Time Series (5min)" sample: [
			"2025-11-18 11:40:00" → 293.1681 (open),
			"2025-11-18 11:45:00" → 293.5950,
			"2025-11-18 11:50:00" → 293.0350
		]
	}
	```
- Free Tier: 5 requests/minute, 500/day per key (unchanged). Add retry queue + caching to stay under burst limits.
- Notes: Response returned within ~1.5s; no throttling seen. Include exponential backoff + local cache for production.

## Yahoo Finance via yfinance
- Library: `yfinance` 0.2.66 inside project venv (`.venv`), Python 3.12.10.
- Script: `api_validation/yfinance_sample.py` (TSLA daily 1y + 1m 5d) executed successfully.
- Output Highlights:
	- Daily fetch returned 250 rows (2024-11-19 → 2025-11-18). Sample row shows OHLCV for 2024-11-19.
	- 1-minute fetch returned 1,950 rows covering 2025-11-12 14:30 UTC → 2025-11-18 20:59 UTC.
	- FutureWarning noted about `auto_adjust`; stick with explicit `auto_adjust=False` when precision required.
- Rate Limit: Still unofficial; respect `period`/`interval` combos and add caching/backoff when looping across symbols.

## CoinGecko
- Endpoint Ping: `https://api.coingecko.com/api/v3/ping`
- Command: `Invoke-RestMethod` via PowerShell.
- Response: `{"gecko_says": "(V3) To the Moon!"}` within ~200ms (subjectively instantaneous).
- Free Tier: 50 calls/minute; recommend 1–5s cache even for BTC/ETH tiles.

## Caching Strategy Summary
TTL Examples:
- Real-time quotes: 5s
- Watchlist: 15s
- Historical OHLC: 1h
Batch requests (Alpha Vantage intraday and Finnhub quotes) to reduce overhead.

## Recent Enhancements (2025-11-19)
- Added persistent artifacts under `api_validation/samples/` for every provider (Alpha Vantage, CoinGecko, Finnhub REST/WS, yfinance daily + intraday).
- Upgraded `api_validation/yfinance_sample.py` to a CLI with symbol/period flags plus timing + CSV output controls.
- Upgraded `api_validation/finnhub_ws_test.py` with configurable symbols/durations, jsonl logging, and throughput stats.
- Introduced `api_validation/run_smoke.py`, a Python smoke runner that hits Alpha Vantage, CoinGecko, Finnhub (REST + WebSocket), and yfinance in one go; designed for CI usage (requires `ALPHAVANTAGE_API_KEY` + `FINNHUB_API_KEY` in env).

## Next Validation Steps
1. Wrap Finnhub REST/WebSocket calls in retry + exponential backoff helpers; document reconnect strategy.
2. Implement shared rate-limit guard (token bucket) for Alpha Vantage + Finnhub REST usage.
3. Extend smoke runner to emit structured summaries (JSON) for CI dashboards and wire into upcoming backend build pipeline.

## Risks / Notes
- Finnhub & Alpha Vantage strict rate limits → must implement request queue & key rotation (future multi-key support).
- WebSocket disconnections need retry + backoff.
- yfinance is scraping-dependent; fallback to Alpha Vantage for reliability.
- CoinGecko occasional spikes; implement simple retry (3 attempts, jitter).

## Preliminary Conclusions
- Alpha Vantage production key validated; intraday data accessible and performant enough for queued backtests (strict rate limits still apply).
- CoinGecko reachable and responsive; suitable for spot crypto tiles with modest caching.
- yfinance library functioning locally; delivers daily + 1m granularity for TSLA across ~1 year / 5 days respectively.
- Finnhub REST + WebSocket both reachable with provided key; WebSocket streaming confirmed via `BINANCE:BTCUSDT` even during equity off-hours.

## Raw Response Notes
- Alpha Vantage + CoinGecko outputs captured via terminal (see command history above). Plan to persist raw JSON/text in future iteration.
- yfinance sample output logged in terminal; consider redirecting to timestamped file for reproducibility.
- Finnhub REST JSON + WebSocket transcript currently only in terminal logs; next pass should persist to `api_validation/samples/finnhub_rest.json` & `.../finnhub_ws.jsonl`.

---
Update this file after each endpoint test with actual response snippets.
