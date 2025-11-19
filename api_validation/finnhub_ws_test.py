from __future__ import annotations

import argparse
import asyncio
import json
import os
import time
from pathlib import Path
from typing import Iterable

import websockets


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Subscribe to Finnhub WebSocket and print timing metrics."
    )
    parser.add_argument(
        "--symbols",
        nargs="+",
        default=["TSLA", "SPY", "BINANCE:BTCUSDT"],
        help="Symbols to subscribe to (default: TSLA SPY BINANCE:BTCUSDT)",
    )
    parser.add_argument(
        "--duration",
        type=int,
        default=12,
        help="How long to listen for messages in seconds (default: 12)",
    )
    parser.add_argument(
        "--recv-timeout",
        type=float,
        default=5.0,
        help="Timeout waiting for messages before logging a warning (default: 5s)",
    )
    parser.add_argument(
        "--ping-interval",
        type=float,
        default=15.0,
        help="WebSocket ping interval in seconds (default: 15)",
    )
    parser.add_argument(
        "--ping-timeout",
        type=float,
        default=15.0,
        help="WebSocket ping timeout in seconds (default: 15)",
    )
    parser.add_argument(
        "--log-path",
        type=Path,
        help="Optional path to append JSON messages (one per line)",
    )
    return parser.parse_args()


def require_key() -> str:
    key = os.environ.get("FINNHUB_API_KEY")
    if not key:
        raise RuntimeError("FINNHUB_API_KEY is not set in environment")
    return key


async def stream_quotes(args: argparse.Namespace) -> None:
    token = require_key()
    url = f"wss://ws.finnhub.io?token={token}"
    print(f"[INFO] Connecting to {url}")

    log_file = None
    if args.log_path:
        args.log_path.parent.mkdir(parents=True, exist_ok=True)
        log_file = args.log_path.open("w", encoding="utf-8")
        print(f"[INFO] Logging messages to {args.log_path}")

    try:
        connect_start = time.perf_counter()
        async with websockets.connect(
            url,
            ping_interval=args.ping_interval,
            ping_timeout=args.ping_timeout,
        ) as ws:
            connect_elapsed = time.perf_counter() - connect_start
            print(f"[INFO] WebSocket connected in {connect_elapsed:.2f}s")

            for symbol in args.symbols:
                payload = json.dumps({"type": "subscribe", "symbol": symbol})
                await ws.send(payload)
                print(f"[INFO] Subscribed: {symbol}")

            start = time.perf_counter()
            msg_count = 0
            while time.perf_counter() - start < args.duration:
                try:
                    message = await asyncio.wait_for(ws.recv(), timeout=args.recv_timeout)
                except asyncio.TimeoutError:
                    print(f"[WARN] No data for {args.recv_timeout:.1f}s window; continuing")
                    continue

                msg_count += 1
                if msg_count <= 5:
                    print(f"[DATA] {message}")
                if log_file:
                    log_file.write(message + "\n")

            throughput = msg_count / max(args.duration, 1)
            print(
                f"[INFO] Received {msg_count} messages in {args.duration}s "
                f"(~{throughput:.1f} msg/s)"
            )
    finally:
        if log_file:
            log_file.close()


def main() -> int:
    args = parse_args()
    asyncio.run(stream_quotes(args))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
