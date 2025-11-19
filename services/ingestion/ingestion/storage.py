from __future__ import annotations

import asyncio
import os
import time
from pathlib import Path
from typing import Iterable

import pandas as pd
import redis.asyncio as redis
from loguru import logger


class RedisPublisher:
    def __init__(self, url: str, stream: str, maxlen: int) -> None:
        self._redis = redis.from_url(url, decode_responses=False)
        self.stream = stream
        self.maxlen = maxlen

    async def publish(self, rows: Iterable[dict]) -> None:
        for row in rows:
            payload = {k: str(v) for k, v in row.items()}
            await self._redis.xadd(self.stream, payload, maxlen=self.maxlen, approximate=True)

    async def close(self) -> None:
        await self._redis.close()


class ParquetWriter:
    def __init__(self, directory: Path, batch_size: int = 200) -> None:
        self.directory = directory
        self.batch_size = batch_size
        self._buffer: list[dict] = []
        self.directory.mkdir(parents=True, exist_ok=True)
        self._lock = asyncio.Lock()

    async def write(self, rows: Iterable[dict]) -> None:
        async with self._lock:
            self._buffer.extend(rows)
            if len(self._buffer) >= self.batch_size:
                await self._flush()

    async def flush(self) -> None:
        async with self._lock:
            await self._flush()

    async def _flush(self) -> None:
        if not self._buffer:
            return
        timestamp = int(time.time())
        path = self.directory / f"finnhub_trades_{timestamp}.parquet"
        df = pd.DataFrame(self._buffer)
        df.to_parquet(path, index=False)
        logger.info("Wrote {rows} rows to {path}", rows=len(self._buffer), path=path)
        self._buffer.clear()


async def shutdown_storage(publisher: RedisPublisher, writer: ParquetWriter) -> None:
    await asyncio.gather(publisher.close(), writer.flush())
