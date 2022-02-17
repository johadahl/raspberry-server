## Description

This is a minimalistic and extensible [FastAPI](https://fastapi.tiangolo.com/) template suitable for developing small to medium sized API oriented micro-services.

## Features

- It uses [FastAPI](https://fastapi.tiangolo.com/) framework for API development. FastAPI is a modern, highly performant, web framework for building APIs with Python 3.6+.

- The APIs are served with [Gunicorn](https://gunicorn.org/) server with multiple [Uvicorn](https://www.uvicorn.org/) workers. Uvicorn is a lightning-fast "ASGI" server. It runs asynchronous Python web code in a single process.

- Simple reverse-proxying with [Caddy](https://caddyserver.com/docs/).

- OAuth2 (with hashed password and Bearer with JWT) based authentication (TODO)

- [CORS (Cross Origin Resource Sharing)](https://fastapi.tiangolo.com/tutorial/cors/) enabled.

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
python3.9 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt && pip install -r requirements-dev.txt
uvicorn app.main:app --port 5001 --reload
```

### Check the APIs

- To play around with the APIs, go to the following link on your browser:

  ```
  http://localhost:5001/docs
  ```

- Press the `authorize` button on the right and add _username_ and _password_. The APIs use OAuth2 (with hashed password and Bearer with JWT) based authentication. In this case, the username and password is `ubuntu` and `debian` respectively.

- Then select any of the `api_a` or `api_b` APIs and put an integer in the number box and click the `authorize` button.

- Hitting the API should give a json response.

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

## Resources

- [Deploying APIs built with FastAPI](https://fastapi.tiangolo.com/deployment/)
- [Reverse proxying with Caddy](https://caddyserver.com/docs/caddyfile/directives/reverse_proxy)
- [Dockerised Flask app template](https://github.com/rednafi/fastapi-nano)
