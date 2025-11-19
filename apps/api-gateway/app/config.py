from __future__ import annotations

import functools
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = Field(..., env="DATABASE_URL")
    redis_url: str = Field(..., env="REDIS_URL")

    class Config:
        env_file = "../../.env"
        env_file_encoding = "utf-8"


@functools.lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
