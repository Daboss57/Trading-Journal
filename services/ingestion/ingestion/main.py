from __future__ import annotations

import argparse
import asyncio

from loguru import logger

from .config import Settings, get_settings
from .finnhub_ws import FinnhubStream


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Ingestion service entry point")
    parser.add_argument("--duration", type=int, default=30, help="Seconds to keep the Finnhub stream alive")
    parser.add_argument("--symbols", nargs="*", help="Override symbols from settings")
    return parser.parse_args()


def run_cli() -> None:
    args = parse_args()
    settings = get_settings()
    if args.symbols:
        settings.symbols = args.symbols

    logger.remove()
    logger.add(lambda msg: print(msg, end=""), level=settings.log_level)

    stream = FinnhubStream(settings)
    asyncio.run(stream.run(duration=args.duration))


if __name__ == "__main__":
    run_cli()
