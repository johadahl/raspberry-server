from datetime import datetime
from http import HTTPStatus
from unittest.mock import AsyncMock, MagicMock

import httpx
import pytest

from app.core.init_app import init_controllers
from app.entities.alarm import AlarmConfig
from app.main import app as app_


@pytest.fixture
async def app():
    app_.db = MagicMock()
    app_.alarm_repository = AsyncMock()
    app_.scheduler = AsyncMock()
    init_controllers(app_)
    return app_


@pytest.fixture
async def test_client(app):
    async with httpx.AsyncClient(app=app, base_url="http://testserver") as client:
        yield client


@pytest.mark.asyncio
async def test_get_config(test_client, app):
    app.alarm_repository.get.return_value = AlarmConfig(
        time="10:01", active=True, id=1, timestamp="2022-02-17T20:30:05.728976"
    )
    response = await test_client.get("/v1/alarm/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "id": 1,
        "timestamp": "2022-02-17T20:30:05.728976",
        "time": "10:01",
        "active": True,
    }


@pytest.mark.asyncio
async def test_create_new_config(app, test_client):
    app.alarm_repository.get.return_value = None

    response = await test_client.post(
        "/v1/alarm/", json={"active": "False", "time": "11:00"}
    )
    response_json = response.json()

    assert response.status_code == HTTPStatus.OK
    assert response_json["time"] == "11:00"
    assert response_json["active"] == False
    assert app.alarm_repository.create.call_count == 1
    assert app.alarm_repository.update.call_count == 0


@pytest.mark.asyncio
async def test_update_config(app, test_client):
    app.alarm_repository.get.return_value = AlarmConfig(
        time="10:01", active=True, id=1, timestamp="2022-02-17T20:30:05.728976"
    )

    response = await test_client.post(
        "/v1/alarm/", json={"active": "False", "time": "11:00"}
    )
    response_json = response.json()

    assert response.status_code == HTTPStatus.OK
    assert response_json["time"] == "11:00"
    assert response_json["active"] == False
    assert app.alarm_repository.create.call_count == 0
    assert app.alarm_repository.update.call_count == 1
