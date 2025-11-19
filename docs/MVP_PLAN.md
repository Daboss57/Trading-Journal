# MVP Execution Plan

**Goal:** Ship a usable paper-trading + backtesting workspace with live market data, strategy journaling, and dashboards aligned to the wireframes.

## 1. MVP Scope Overview
| Domain | Must-Haves |
| --- | --- |
| **Authentication & Accounts** | Clerk/NextAuth login, single account, role = trader. |
| **Market Data** | Real-time watchlist tiles (top symbols) powered by Finnhub WS cache + yfinance fallbacks; Alpha Vantage intraday snapshots for historical view. |
| **Paper Trading** | Simulated order ticket (market/limit), open positions, P&L calc, activity log. |
| **Backtesting** | Strategy builder (config form) sending jobs to workers; display results summary + equity curve dataset. |
| **Analytics & Journaling** | Trade history table, ability to tag trades/notes. |
| **Infrastructure** | CI smoke, Docker Compose dev stack, Terraform dev env, observability hooks. |

## 2. Milestones & Exit Criteria
1. **Milestone A – Data Foundation (Week 1-2)**
   - Finnhub ingestion service streaming into Redis Streams + Blob parquet dumps.
   - API gateway exposes `/health`, `/watchlist`, `/quotes/{symbol}` hitting Redis/Pg fallback.
   - Smoke runner green in CI w/ secrets.
2. **Milestone B – Trading API (Week 3-4)**
   - Postgres schema for accounts, watchlists, orders, fills, trades.
   - Paper trading engine service (can live in workers) matching synthetic orders vs cached prices.
   - FastAPI endpoints for watchlist CRUD + order placement + positions summary.
3. **Milestone C – Backtesting Loop (Week 5)**
   - Celery workers execute strategy configs via `strategy-engine` package, persist results, emit summary.
   - Frontend backtest builder UI hitting endpoints, results view w/ charts (stubbed data acceptable early).
4. **Milestone D – UX Polish & Observability (Week 6)**
   - Core wireframe screens implemented (dashboard, watchlist, order ticket, analytics).
   - Metrics/logging dashboards, alerting, onboarding docs updated.

Each milestone is “done” when Compose passes, CI smoke passes, and documented demo steps succeed.

## 3. Immediate Engineering Backlog (Next 2 Weeks)
| Priority | Task | Owner Hint | Output |
| --- | --- | --- | --- |
| P0 | Wire Redis + Postgres containers into FastAPI via settings to prep for real data | Backend | Config files + health checks hitting both services. |
| P0 | Extend ingestion service to push Finnhub ticks into Redis Streams (`md:finnhub:trades`) and persist rolling parquet to Blob mock | Data/Platform | Updated `services/ingestion` with Redis writer + storage adapter. |
| P0 | Define Postgres schema + Alembic migrations for accounts/watchlists/orders/backtests | Backend | `apps/api-gateway/migrations` module plus ERD doc. |
| P1 | Implement watchlist CRUD + price snapshot endpoints using market-clients fallback | Backend | FastAPI routes + tests. |
| P1 | Frontend consume watchlist API, render live tiles from WebSocket + REST fallback | Frontend | React hooks + Zustand store powering dashboard/watchlist wireframes. |
| P1 | Celery worker skeleton using `strategy-engine.run_backtest` with mock data | Workers | Service that accepts job payload + stores result stub. |
| P2 | Paper-trading order execution loop referencing cached quotes + storing fills | Backend/Workers | Module under `services/workers` with tests + API integration. |
| P2 | Backtest results page hooking to new API endpoints | Frontend | Chart + table using fetched metrics. |

Track backlog via GitHub issues reflecting these rows. Owners can adjust priority as dependencies resolve.

## 4. Recommended Execution Order
1. **Platform plumbing** – finalize Compose, secrets management, Terraform dev rollout, and shared libs (done or in-flight). Ensures subsequent services have stable targets.
2. **Data ingestion + cache** – finish Finnhub stream writer + Alpha Vantage snapshot jobs before API/UX work so real data is available.
3. **Database + domain models** – design schema/migrations immediately after ingestion so API endpoints have persistence.
4. **Trading API** – build watchlist/order/backtest endpoints once data + schema are live; include unit/integration tests.
5. **Workers & strategy engine** – wire Celery/backtest jobs leveraging the schema, enabling asynchronous workloads.
6. **Frontend integration** – hook pages to new endpoints/WebSockets, starting with dashboard/watchlist, then order entry, analytics, backtests.
7. **Polish & observability** – instrument logging/metrics, add alerts, refine UX per wireframes, and document onboarding.

Each step unblocks the next, minimizing rework and aligning with the milestone cadence.
