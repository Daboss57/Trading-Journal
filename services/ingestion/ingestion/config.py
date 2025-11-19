from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    finnhub_api_key: str = Field(..., env="FINNHUB_API_KEY")
    symbols: list[str] = Field(default_factory=lambda: ["BINANCE:BTCUSDT"])
    ws_url: str = "wss://ws.finnhub.io"
    log_level: str = "INFO"
    redis_url: str = Field("redis://localhost:6379/0", env="REDIS_URL")
    redis_stream: str = Field("md:finnhub:trades", env="FINNHUB_REDIS_STREAM")
    redis_stream_maxlen: int = Field(5000, env="FINNHUB_STREAM_MAXLEN")
    parquet_dir: Path = Field(Path("storage/parquet"), env="PARQUET_DIR")
    parquet_batch_size: int = Field(200, env="PARQUET_BATCH_SIZE")

    class Config:
        env_file = "../../.env"
        env_file_encoding = "utf-8"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
