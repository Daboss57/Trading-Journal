from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

import requests


def ensure_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Environment variable {name} is required for this test")
    return value


def write_json(out_path: Path, payload: dict) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2))
    print(f"[INFO] Wrote {out_path}")


def check_alpha_vantage(symbol: str, key: str, out_dir: Path) -> None:
    print(f"[STEP] Alpha Vantage REST for {symbol}")
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": "5min",
        "apikey": key,
    }
    resp = requests.get("https://www.alphavantage.co/query", params=params, timeout=20)
    resp.raise_for_status()
    data = resp.json()
    sample = list(data.get("Time Series (5min)", {}).items())[:3]
    print(f"[INFO] Retrieved {len(sample)} sample points")
    timestamp = int(time.time())
    out_path = out_dir / f"alpha_vantage_{symbol}_{timestamp}.json"
    write_json(out_path, data)


def check_coingecko(out_dir: Path) -> None:
    print("[STEP] CoinGecko ping")
    resp = requests.get("https://api.coingecko.com/api/v3/ping", timeout=10)
    resp.raise_for_status()
    data = resp.json()
    print(f"[INFO] Response: {data}")
    out_path = out_dir / f"coingecko_ping_{int(time.time())}.json"
    write_json(out_path, data)


def check_finnhub_rest(symbol: str, key: str, out_dir: Path) -> None:
    print(f"[STEP] Finnhub REST for {symbol}")
    params = {"symbol": symbol, "token": key}
    resp = requests.get("https://finnhub.io/api/v1/quote", params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    print(f"[INFO] Quote: {data}")
    out_path = out_dir / f"finnhub_{symbol}_{int(time.time())}.json"
    write_json(out_path, data)


def run_subprocess(cmd: list[str]) -> None:
    print(f"[STEP] Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run all API validation checks sequentially")
    parser.add_argument("--alpha-symbol", default="IBM", help="Symbol for Alpha Vantage test")
    parser.add_argument("--yf-symbol", default="TSLA", help="Symbol for yfinance test")
    parser.add_argument("--finnhub-symbol", default="TSLA", help="Symbol for Finnhub REST test")
    parser.add_argument(
        "--out-dir",
        default="api_validation/samples/smoke",
        help="Directory to store smoke artifacts",
    )
    parser.add_argument(
        "--yf-args",
        nargs=argparse.REMAINDER,
        help="Extra arguments passed to yfinance_sample.py",
    )
    parser.add_argument(
        "--ws-duration",
        type=int,
        default=6,
        help="Duration for Finnhub WebSocket smoke run",
    )
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    alpha_key = ensure_env("ALPHAVANTAGE_API_KEY")
    finnhub_key = ensure_env("FINNHUB_API_KEY")

    check_alpha_vantage(args.alpha_symbol, alpha_key, out_dir)
    check_coingecko(out_dir)
    check_finnhub_rest(args.finnhub_symbol, finnhub_key, out_dir)

    yf_cmd = [
        sys.executable,
        "api_validation/yfinance_sample.py",
        "--symbol",
        args.yf_symbol,
        "--out-dir",
        str(out_dir),
    ]
    if args.yf_args:
        yf_cmd.extend(args.yf_args)
    run_subprocess(yf_cmd)

    ws_cmd = [
        sys.executable,
        "api_validation/finnhub_ws_test.py",
        "--symbols",
        args.finnhub_symbol,
        "BINANCE:BTCUSDT",
        "--duration",
        str(args.ws_duration),
        "--log-path",
        str(out_dir / "finnhub_ws.jsonl"),
    ]
    run_subprocess(ws_cmd)

    print("[SUCCESS] All smoke checks completed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
