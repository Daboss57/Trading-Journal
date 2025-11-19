# Trading Journal Monorepo

Engineering workspace for the day-trading paper trading + backtesting platform.

## Structure
| Path | Purpose |
| --- | --- |
| `apps/frontend` | Next.js UI aligning with the dashboard/watchlist wireframes. |
| `apps/api-gateway` | FastAPI gateway that fronts ingestion + worker services. |
| `packages/strategy-engine` | Shared Python library for deterministic backtesting. |
| `packages/market-clients` | Typed wrappers for Finnhub, Alpha Vantage, CoinGecko, etc. |
| `services/ingestion` | WebSocket + REST pollers handling market data ingestion. |
| `services/workers` | Celery workers for backtests, paper fills, analytics jobs. |
| `infra/terraform` | Infrastructure-as-code modules for Azure resources. |
| `infra/pipelines` | CI/CD workflow definitions and shared automation scripts. |
| `docs` | PRD, technical setup, onboarding, and design references. |
| `api_validation` | Existing API validation scripts + smoke runner, reused in CI. |

## Getting Started
1. Install prerequisites (Python 3.12, Node 20, pnpm 9, uv, Docker).
2. Install dependencies:
   ```bash
   pnpm install
   uv sync
   ```
3. Run sanity checks:
   ```bash
   pnpm dev --filter @trading-journal/frontend
   uv run --project apps/api-gateway uvicorn app.main:app --reload
   python api_validation/run_smoke.py --ws-duration 3
   ```
4. Review `docs/ONBOARDING.md` + `docs/TECHNICAL_SETUP.md` for deeper context.

## Docker Compose Dev Stack
Fast path to bring up the placeholder frontend, FastAPI gateway, Postgres, and Redis:

```powershell
Copy-Item .env.example .env
docker compose up --build
```

Services:
- `frontend`: Next.js dev server on http://localhost:3000
- `api`: FastAPI on http://localhost:8000
- `postgres`: connection string `postgresql://trader:traderpass@localhost:5432/tradingjournal`
- `redis`: default port 6379

## CI Secrets
GitHub Actions expects the following repository secrets to run the smoke suite:
- `ALPHAVANTAGE_API_KEY`
- `FINNHUB_API_KEY`

If either secret is missing, the smoke step is skipped automatically.
