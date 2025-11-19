# Workers Service

Executes asynchronous jobs: strategy backtests, paper-trade fills, report generation.

## Stack
- Celery + Redis broker (initially) with UVicorn-managed FastAPI gateway dispatching jobs.
- Uses `packages/strategy-engine` for deterministic calculations.

## TODO
- Define Celery tasks + routing keys.
- Add Temporal evaluation spike for long-running strategies.
- Instrument with OpenTelemetry traces.
