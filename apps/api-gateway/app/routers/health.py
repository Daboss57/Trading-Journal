from __future__ import annotations

from fastapi import APIRouter, Depends

from ..deps import get_redis_pool, get_db_connection

router = APIRouter(prefix="/health", tags=["system"])


@router.get("", summary="Composite health check")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/redis", summary="Redis connectivity")
async def redis_health(redis_client = Depends(get_redis_pool)) -> dict[str, str]:
    pong = await redis_client.ping()
    return {"status": "ok" if pong else "degraded"}


@router.get("/postgres", summary="Postgres connectivity")
async def postgres_health(conn = Depends(get_db_connection)) -> dict[str, str]:
    await conn.execute("SELECT 1")
    await conn.close()
    return {"status": "ok"}
