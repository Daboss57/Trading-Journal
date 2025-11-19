from __future__ import annotations

import asyncpg
import redis.asyncio as redis
from functools import lru_cache

from .config import get_settings


@lru_cache(maxsize=1)
def get_redis_pool() -> redis.Redis:
    settings = get_settings()
    return redis.from_url(settings.redis_url, decode_responses=True)


async def get_db_connection() -> asyncpg.Connection:
    settings = get_settings()
    return await asyncpg.connect(settings.database_url)
