# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-slim AS base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    UV_LINK_MODE=copy \
    PATH="/root/.local/bin:$PATH"

# Dependências do sistema
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    ca-certificates \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalação do uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

WORKDIR /app

# Instalar dependências primeiro para aproveitar o cache
COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-install-project

# Copiar aplicação
COPY . .

# Instalar o projeto
RUN uv sync --frozen

EXPOSE 8000

CMD ["uv", "run", "fastapi", "dev", "--host", "0.0.0.0", "--port", "8000"]