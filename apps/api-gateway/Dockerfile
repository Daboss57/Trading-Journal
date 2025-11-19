# syntax=docker/dockerfile:1.7
FROM python:3.12-slim

ENV UV_NO_SYNC_PROGRESS=1

RUN pip install --no-cache-dir uv

WORKDIR /workspace/apps/api-gateway

COPY apps/api-gateway/pyproject.toml ./
COPY apps/api-gateway/app ./app

RUN uv sync --frozen --no-dev

EXPOSE 8000
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
