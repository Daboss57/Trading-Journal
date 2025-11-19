from __future__ import annotations

import asyncio
import json
import time
from typing import Iterable

from loguru import logger
from market_clients import FinnhubClient
import websockets

from .config import Settings
from .storage import ParquetWriter, RedisPublisher, shutdown_storage


class FinnhubStream:
    """Handles a single Finnhub WebSocket session and basic logging."""

    def __init__(
        self,
        settings: Settings,
        rest_client: FinnhubClient | None = None,
        publisher: RedisPublisher | None = None,
        parquet_writer: ParquetWriter | None = None,
    ) -> None:
        self.settings = settings
        self.rest_client = rest_client or FinnhubClient(api_key=settings.finnhub_api_key)
        self._message_count = 0
        self.publisher = publisher or RedisPublisher(
            url=settings.redis_url,
            stream=settings.redis_stream,
            maxlen=settings.redis_stream_maxlen,
        )
        self.parquet_writer = parquet_writer or ParquetWriter(
            directory=settings.parquet_dir,
            batch_size=settings.parquet_batch_size,
        )

    async def run(self, *, duration: int | None = None) -> None:
        url = f"{self.settings.ws_url}?token={self.settings.finnhub_api_key}"
        logger.info("Connecting to Finnhub WS {url}", url=url)
        start = time.perf_counter()
        async with websockets.connect(url, ping_interval=15, ping_timeout=10) as ws:
            await self._bootstrap(ws)
            await self._consume(ws, duration=duration)
        elapsed = time.perf_counter() - start
        logger.info("Closed Finnhub WS session after {elapsed:.1f}s with {count} messages", elapsed=elapsed, count=self._message_count)
        await shutdown_storage(self.publisher, self.parquet_writer)

    async def _bootstrap(self, ws: websockets.WebSocketClientProtocol) -> None:
        await self._subscribe(ws, self.settings.symbols)
        snapshot = self.rest_client.quote(self.settings.symbols[0])
        logger.debug("REST quote for {symbol}: {snapshot}", symbol=self.settings.symbols[0], snapshot=snapshot)

    async def _subscribe(self, ws: websockets.WebSocketClientProtocol, symbols: Iterable[str]) -> None:
        for symbol in symbols:
            payload = json.dumps({"type": "subscribe", "symbol": symbol})
            await ws.send(payload)
            logger.info("Subscribed to {symbol}", symbol=symbol)

    async def _consume(self, ws: websockets.WebSocketClientProtocol, *, duration: int | None) -> None:
        deadline = time.monotonic() + duration if duration else None
        while True:
            if deadline and time.monotonic() >= deadline:
                logger.info("Duration reached; stopping stream")
                break
            try:
                message = await asyncio.wait_for(ws.recv(), timeout=30)
            except asyncio.TimeoutError:
                logger.warning("Finnhub stream idle for 30s; sending ping")
                await ws.ping()
                continue
            self._message_count += 1
            await self._handle_message(message)

    async def _handle_message(self, raw_message: str) -> None:
        logger.debug("Finnhub payload #{count}: {message}", count=self._message_count, message=raw_message)
        data = json.loads(raw_message)
        if data.get("type") != "trade":
            return
        trades = [
            {
                "symbol": trade.get("s"),
                "price": trade.get("p"),
                "volume": trade.get("v"),
                "timestamp": trade.get("t"),
                "conditions": ",".join(trade.get("c", [])),
                "source": "finnhub",
            }
            for trade in data.get("data", [])
        ]
        if not trades:
            return
        await self.publisher.publish(trades)
        await self.parquet_writer.write(trades)

    @property
    def message_count(self) -> int:
        return self._message_count
