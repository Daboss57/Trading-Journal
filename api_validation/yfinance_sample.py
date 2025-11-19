from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

import yfinance as yf


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(
		description="Download sample historical data via yfinance with timing metrics."
	)
	parser.add_argument("--symbol", default="TSLA", help="Ticker to download (default: TSLA)")
	parser.add_argument("--daily-period", default="1y", help="Period for daily download (default: 1y)")
	parser.add_argument("--daily-interval", default="1d", help="Interval for daily download (default: 1d)")
	parser.add_argument(
		"--intraday-period",
		default="5d",
		help="Period for intraday download (default: 5d because 1m data limited)",
	)
	parser.add_argument(
		"--intraday-interval", default="1m", help="Interval for intraday download (default: 1m)"
	)
	parser.add_argument(
		"--out-dir",
		default="api_validation/samples",
		help="Directory to save CSV outputs (default: api_validation/samples)",
	)
	parser.add_argument(
		"--auto-adjust",
		action="store_true",
		help="Enable yfinance auto_adjust (default False to preserve raw OHLC)",
	)
	parser.add_argument(
		"--no-save",
		action="store_true",
		help="Skip writing CSV outputs (still prints summary)",
	)
	return parser.parse_args()


def fetch(symbol: str, period: str, interval: str, label: str, args: argparse.Namespace) -> int:
	print(f"[INFO] Fetching {label} data for {symbol} (period={period}, interval={interval})")
	start = time.perf_counter()
	data = yf.download(
		symbol,
		period=period,
		interval=interval,
		progress=False,
		auto_adjust=args.auto_adjust,
	)
	elapsed = time.perf_counter() - start
	if data.empty:
		print(f"[WARN] No data returned for {symbol} ({label}). Elapsed {elapsed:.2f}s")
		return 0

	head = data.head(3)
	tail = data.tail(3)
	print("[INFO] Head:")
	print(head)
	print("[INFO] Tail:")
	print(tail)
	print(f"[INFO] Rows: {len(data)}; First: {data.index[0]}; Last: {data.index[-1]}")
	print(f"[INFO] Download finished in {elapsed:.2f}s")

	if not args.no_save:
		out_dir = Path(args.out_dir)
		out_dir.mkdir(parents=True, exist_ok=True)
		out_path = out_dir / f"{symbol}_{label}_{period}_{interval}.csv"
		data.to_csv(out_path)
		print(f"[INFO] Saved CSV -> {out_path}")

	return len(data)


def main() -> int:
	args = parse_args()
	daily_rows = fetch(args.symbol, args.daily_period, args.daily_interval, "daily", args)
	intraday_rows = fetch(
		args.symbol, args.intraday_period, args.intraday_interval, "intraday", args
	)
	print(
		f"[INFO] Summary: daily rows={daily_rows}, intraday rows={intraday_rows}, "
		f"auto_adjust={'on' if args.auto_adjust else 'off'}"
	)
	return 0


if __name__ == "__main__":
	sys.exit(main())