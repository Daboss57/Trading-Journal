# API Gateway (FastAPI)

FastAPI service that frontends the market data adapters, backtesting engine, and paper-trading event loop.

## Local Dev

```bash
uv sync
uv run uvicorn app.main:app --reload
```

## TODO
- Wire auth middleware + Clerk/NextAuth JWT validation.
- Stream real quotes from Redis pub/sub once ingestion service is live.
- Add GraphQL route + OpenAPI examples.
