# syntax=docker/dockerfile:1.7
FROM node:20-bookworm

ENV PNPM_HOME=/root/.local/share/pnpm
ENV PATH="$PNPM_HOME:$PATH"

RUN corepack enable

WORKDIR /workspace

COPY package.json pnpm-workspace.yaml ./
COPY apps/frontend/package.json apps/frontend/
COPY apps/frontend/tsconfig.json apps/frontend/
COPY apps/frontend/next.config.mjs apps/frontend/
COPY apps/frontend/next-env.d.ts apps/frontend/
COPY apps/frontend/app apps/frontend/app
COPY apps/frontend/public apps/frontend/public

RUN pnpm install --filter @trading-journal/frontend... --prefer-offline

CMD ["pnpm", "dev", "--filter", "@trading-journal/frontend", "--hostname", "0.0.0.0"]
