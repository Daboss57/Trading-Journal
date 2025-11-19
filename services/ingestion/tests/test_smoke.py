from __future__ import annotations

import asyncio
import os
import tempfile
from pathlib import Path

from ingestion.storage import ParquetWriter, RedisPublisher

TEST_ROWS = [
    {"symbol": "TSLA", "price": 250.12, "volume": 10, "timestamp": 1_734_000_000, "conditions": "t", "source": "ci"},
    {"symbol": "TSLA", "price": 250.32, "volume": 12, "timestamp": 1_734_000_005, "conditions": "t", "source": "ci"},
]


async def run_smoke() -> None:
    redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    stream_name = os.getenv("REDIS_SMOKE_STREAM", "md:ci:smoke")
    publisher = RedisPublisher(redis_url, stream_name, maxlen=200)

    try:
        with tempfile.TemporaryDirectory(prefix="ingestion-ci-") as tmpdir:
            writer = ParquetWriter(Path(tmpdir), batch_size=len(TEST_ROWS))
            await publisher.publish(TEST_ROWS)
            await writer.write(TEST_ROWS)
            await writer.flush()

            length = await publisher._redis.xlen(stream_name)
            if length < len(TEST_ROWS):
                raise RuntimeError(f"Redis stream {stream_name} missing entries; expected >= {len(TEST_ROWS)}, got {length}")

            parquet_files = list(Path(tmpdir).glob("*.parquet"))
            if not parquet_files:
                raise RuntimeError("Parquet writer did not emit any files")

    finally:
        await publisher.close()


if __name__ == "__main__":
    asyncio.run(run_smoke())
