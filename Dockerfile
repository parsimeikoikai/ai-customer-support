# Stage 1: build the dashboard (Vite + React + shadcn/ui) into static files.
FROM node:24-alpine AS dashboard
WORKDIR /dashboard
COPY dashboard/package.json dashboard/package-lock.json ./
RUN npm ci
COPY dashboard/ ./
RUN npm run build

# Stage 2: the Python backend, which also serves the built dashboard.
FROM python:3.13-slim
COPY --from=ghcr.io/astral-sh/uv:0.11.24 /uv /usr/local/bin/uv

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# Install dependencies first, so code changes do not reinstall them.
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

COPY app/ ./app/
COPY knowledge_base/ ./knowledge_base/
COPY scripts/ ./scripts/
COPY --from=dashboard /dashboard/dist ./dashboard/dist

# Run as a non-root user.
RUN useradd --create-home appuser
USER appuser

EXPOSE 8080
CMD ["fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "8080"]
