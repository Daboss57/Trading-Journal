# Technical Setup Plan

**Date:** 2025-11-18  
**Author:** GitHub Copilot (w/ Noel)  
**Context:** PRD + wireframes approved. API validation + smoke tests completed (see `api_validation/API_VALIDATION.md`). This document locks the initial architecture, tooling, and environment plan so engineering can start implementation with confidence.

---

## 1. Objectives & Inputs
- Deliver a concrete stack + infrastructure blueprint for the day-trading/backtesting platform outlined in the PRD and wireframes.
- Leverage validated data providers (Finnhub, Alpha Vantage, Yahoo Finance via `yfinance`, CoinGecko) and the new smoke runner (`api_validation/run_smoke.py`).
- Define environments, repository structure, CI/CD, security, and observability guardrails.
- Keep the design modular so we can scale from MVP (paper trading + backtests) to live trading later.

Key assumptions:
- **Workload mix:** real-time streaming for watchlists & order tickets, fast analytical queries for performance dashboards, heavy but offline-ish CPU jobs for backtests.
- **Team size:** small full-stack team (2–5 engineers) shipping iteratively.
- **Hosting preference:** Azure (aligns with organization defaults), but components remain portable.

---

## 2. High-Level Architecture
```
[Next.js Frontend]
        |
   (GraphQL/REST)
        |
[FastAPI Gateway] --(Pub/Sub)--> [Strategy & Backtest Workers]
        |                              |
    [Postgres] <--> [Redis] <--> [Task Queue (Celery/Redis Streams)]
        |
 [Data Lake / Blob Storage]
        ^
        |
[Market Data Services]
(Finnhub WS ingest, Alpha Vantage batch, CoinGecko ping, yfinance snapshot)
```

Core domains:
1. **Client Experience:** Responsive dashboard + mobile views (per wireframes) backed by Next.js 15 + React Server Components for SEO and speed.
2. **Trading API:** FastAPI service exposing REST/GraphQL, orchestrating orders, mock executions, and portfolio state.
3. **Market Data Layer:** Dedicated workers handling WebSocket streaming, rate-limited REST pulls, caching, and persistence.
4. **Backtesting Engine:** Job-oriented service fed by strategy configs; publishes results + telemetry.
5. **Data Platform:** Postgres for transactional data, TimescaleDB extension for price series, Blob Storage for large CSV/Parquet dumps, Redis for caching + pub/sub.

---

## 3. Technology Choices
| Layer | Selection | Rationale |
| --- | --- | --- |
| Frontend | Next.js 15, TypeScript, Tailwind, React Query, Zustand | Hybrid SSR/SPA, strong DX, flexible component model for dense dashboards. |
| WebSockets | `socket.io` gateway on FastAPI via `ASGI` or `wsproto` | Unified push channel for quotes/order updates. |
| API | FastAPI (Python 3.12) | Excellent typing, async-first, reuses data models with ingestion/backtests. |
| Auth | Clerk/NextAuth for client, JWT verified in FastAPI | Rapid auth integration, supports social + email, plus role-based claims. |
| DB | Azure Database for PostgreSQL (with TimescaleDB) | Time-series + relational in one service; managed backups. |
| Cache/Queues | Azure Cache for Redis (Redis 7) | Pub/Sub for streaming to frontend, task queue broker, rate-limit buckets. |
| Object Storage | Azure Blob Storage (Hot tier) | Durable storage for raw API dumps, backtest outputs, CSV exports. |
| Workers | Celery + Redis (short term); evaluate Temporal for orchestration later | Simple to start while giving path to reliable job handling. |
| Backtest Engine | Python module w/ pandas, numpy, vectorbt-lite | Aligns with data science tooling; integrate with Celery for distributed runs. |
| Infra as Code | Terraform + Terragrunt | Consistent environment provisioning + GitOps. |
| CI/CD | GitHub Actions | Already using GitHub; actions integrate with smoke runner + tests. |
| Observability | OpenTelemetry SDK, Azure Monitor, Grafana Cloud | Tracing + metrics from API, ingest, workers. |
| Secrets | Azure Key Vault + Doppler for local dev | Centralized, auditable secret distribution. |

---

## 4. Environments & Deployment Targets
| Environment | Purpose | Hosting |
| --- | --- | --- |
| **Local** | Developer machines using Docker Compose; mocks for market data optional | Compose + `uv`/`pnpm` for package mgmt |
| **Dev** | Shared integration env auto-deployed from `develop` | Azure Container Apps (frontend static export + FastAPI), Azure Postgres, Redis Basic |
| **Staging** | Prod-like env w/ canary data + scheduled smoke | Azure Kubernetes Service (AKS) for multi-container workloads |
| **Prod** | SLA-backed environment with autoscale + global CDN | AKS (backend + workers), Azure Front Door CDN for Next.js, managed DB/cache/Key Vault |

Deployment strategy:
1. Containers built via `docker buildx` multi-arch.
2. GitHub Actions pipeline publishes to Azure Container Registry (ACR).
3. ArgoCD/Flux (optional) syncs manifests to AKS; Container Apps uses GitHub OIDC.
4. Smoke runner (`python api_validation/run_smoke.py`) executes post-deploy, gating rollouts.

---

## 5. Repository Layout (monorepo)
```
tradingJournal/
├── apps/
│   ├── frontend/            # Next.js project
│   └── api-gateway/         # FastAPI service
├── packages/
│   ├── strategy-engine/     # Shared backtest logic
│   └── market-clients/      # Finnhub/AlphaVantage SDK wrappers
├── services/
│   ├── ingestion/           # WebSocket + REST pollers
│   └── workers/             # Celery worker entrypoints
├── infra/
│   ├── terraform/           # IaC modules
│   └── pipelines/           # GitHub Actions workflows
├── docs/
│   ├── PRD.md
│   ├── WIREFRAMES/...
│   └── TECHNICAL_SETUP.md   # (this file)
├── api_validation/          # Existing validation + smoke tooling
├── scripts/                 # Local helper scripts, data seeding
└── .github/workflows/       # CI/CD definitions
```

Tooling defaults:
- **Python:** `uv` for package management, `ruff` + `mypy` for lint/type, `pytest` for tests.
- **Node:** `pnpm`, `eslint`, `biome` (optional) for formatting.
- **Pre-commit:** Format + lint before pushes.
- **Conventional Commits** + `changeset` for versioning packages.

---

## 6. Market Data Integration Blueprint
1. **Finnhub WebSocket Service**
   - Runs as an ASGI app or standalone worker.
   - Maintains persistent connection per symbol group (equities vs crypto) w/ heartbeat + exponential backoff.
   - Writes raw ticks to Redis Streams (`md:finnhub:trades`) and daily Parquet in Blob Storage.
2. **Alpha Vantage Fetcher**
   - Scheduled Celery beat job per symbol list (approx every 5 minutes respecting rate limits + key rotation).
   - Stores last sync metadata in Postgres; raw JSON/CSV in Blob Storage.
3. **Yahoo Finance Snapshotter**
   - Reuses `api_validation/yfinance_sample.py` logic inside `market-clients` package.
   - Runs hourly for watchlist symbols; caches results in Redis for quick UI loads.
4. **CoinGecko Health Check**
   - Simple heartbeat job verifying endpoint availability; results feed into status banner.
5. **Rate Limiting / Secrets**
   - Keys loaded from Key Vault into Kubernetes secrets; rotate via CI.
   - Token-bucket counters stored in Redis hashed by API + symbol to prevent bursts.

---

## 7. Backtesting & Paper Trading Engine
- **Strategy Definition:** JSON/YAML schema stored in Postgres (`strategy_definitions` table) plus versioned Python modules for advanced strategies.
- **Execution:** Celery workers pull jobs, hydrate market data from Blob/Timescale, and run vectorized calculations (pandas, numba when needed).
- **Results Storage:** Summary metrics in Postgres (`backtest_runs`), full equity curves + trade logs in Parquet on Blob; signed URLs feed the UI.
- **Paper Trading Loop:** Event-driven engine that consumes synthetic orders, matches vs live quote cache, and emits fills via Redis pub/sub.
- **Extensibility:** Later swap Celery for Temporal or Dagster for better retry/visibility.

---

## 8. Observability & Reliability
- **Logging:** Structured JSON logs (Loguru for Python, pino for Node). Ship to Azure Monitor + Log Analytics.
- **Metrics:** OpenTelemetry exporter → Prometheus/Grafana dashboards for latency, queue depth, data freshness, smoke runner outcomes.
- **Tracing:** Trace IDs propagated from frontend → backend → workers to debug order lifecycles.
- **Alerts:** PagerDuty hooks for API failure rate, WebSocket disconnect streaks, stale data.
- **Chaos / DR:** Quarterly chaos drills (drop Redis, cut Finnhub connection) and documented runbooks.

---

## 9. Security & Compliance
- **AuthZ:** Role-based + per-account scoping (viewer, trader, admin). Future support for multi-tenant organizations.
- **Secrets:** Managed entirely via Key Vault; local dev uses `.env` generated by Doppler (no raw keys committed).
- **Data Privacy:** Personally identifiable info encrypted at rest (Postgres column-level encryption) + in transit (TLS everywhere).
- **Audit Trails:** Append-only `audit_log` table capturing order actions, login attempts, config changes.
- **Testing:** Security scans via `pip-audit`, `npm audit`, CodeQL, plus dependency review gates in PR.

---

## 10. CI/CD Pipeline Sketch
1. **Pre-push Hooks:** `ruff check`, `pytest -q`, `pnpm test`, `python api_validation/run_smoke.py --ws-duration 3` (optional fast mode).
2. **Pull Request Workflow:**
   - Install dependencies (Python `uv`, Node `pnpm`).
   - Run unit + integration tests.
   - Execute smoke runner against mock environment (real keys via GitHub secrets, read-only).
   - Build Docker images + push to ACR (tagged by commit SHA).
3. **Deployment:**
   - Dev/staging auto-deploy on merge to `develop`/`main` via GitHub Actions + Azure Container Apps/AKS.
   - Prod requires manual approval + success of staging smoke + synthetic backtest.
4. **Post-Deploy Verification:**
   - Trigger `run_smoke.py` against live endpoints.
   - Run `health-check` endpoint to verify migrations, queue consumption, WebSocket status.

---

## 11. Next Steps Checklist
1. Bootstrap repository structure (scaffold folders listed above, add `README.md`, `package.json`, `pyproject.toml`).
2. Containerize existing validation scripts for reuse in CI (small `Dockerfile.smoke`).
3. Write Terraform modules for shared resources (VNet, Postgres, Redis, Key Vault, Blob Storage, Container Registry).
4. Stand up local Docker Compose with Postgres + Redis + FastAPI skeleton + Next.js placeholder page.
5. Implement market-client package with typed wrappers + rate limiting.
6. Build minimal FastAPI gateway: auth stubs, watchlist endpoint hitting Redis cache, pass-through to sample data.
7. Integrate smoke runner into CI (GitHub Actions workflow referencing stored secrets + artifact uploads).
8. Document onboarding steps in `docs/ONBOARDING.md` once scaffolding lands.

Completing the above will transition the project from planning to active development while keeping architecture consistent with the validated APIs and wireframed UX.
