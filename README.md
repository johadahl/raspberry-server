## Description

This is a small [FastAPI](https://fastapi.tiangolo.com/) server for managing the state of my alarm clock running on a Raspberry Pi.

## Features

- It uses [FastAPI](https://fastapi.tiangolo.com/) framework for API development. FastAPI is a modern, highly performant, web framework for building APIs with Python 3.6+.

- The APIs are served with [Gunicorn](https://gunicorn.org/) server with multiple [Uvicorn](https://www.uvicorn.org/) workers. Uvicorn is a lightning-fast "ASGI" server. It runs asynchronous Python web code in a single process.

- Simple reverse-proxying with [Caddy](https://caddyserver.com/docs/).

- OAuth2 (with hashed password and Bearer with JWT) based authentication (TODO)

- Dockerized using [python:3.9-slim-bullseye](https://github.com/docker-library/python/blob/bb68424de76756a2d3dc817f87b1f8640112461f/3.8/bullseye/Dockerfile) and optimized for size and functionality.

## Quickstart

### Prerequisites

Make sure you've got [Docker](https://www.docker.com/) and [Docker Compose V2](https://docs.docker.com/compose/cli-command/) installed on your system.

### Run the App

```bash
docker compose up -d
```

or if you want to run the application locally, without using Docker, then:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt && pip install -r requirements-dev.txt
uvicorn app.main:app --port 5001 --reload
```

### Update dependencies

run 
```bash
./scripts/update_deps.sh
```
## Stack

- [Caddy](https://caddyserver.com/docs/)
- [Docker](https://www.docker.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Gunicorn](https://gunicorn.org/)
- [Httpx](https://www.python-httpx.org/)
- [Pip-tools](https://github.com/jazzband/pip-tools)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Pytest](https://docs.pytest.org/en/latest/)
- [Starlette](https://www.starlette.io/)
- [Uvicorn](https://www.uvicorn.org/)

