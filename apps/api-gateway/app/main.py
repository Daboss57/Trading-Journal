from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI

from .deps import get_redis_pool
from .routers import health


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis_client = get_redis_pool()
    try:
        yield
    finally:
        await redis_client.close()


app = FastAPI(title="Trading Journal API Gateway", version="0.1.0", lifespan=lifespan)


@app.get("/watchlist", tags=["watchlist"])
def sample_watchlist() -> dict[str, list[dict[str, str]]]:
    """Temporary placeholder until real market data wiring is complete."""
    return {
        "data": [
            {"symbol": "TSLA", "price": "248.21", "change": "+1.2%"},
            {"symbol": "NVDA", "price": "129.55", "change": "-0.3%"},
            {"symbol": "AAPL", "price": "198.12", "change": "+0.7%"},
        ]
    }


app.include_router(health.router)
