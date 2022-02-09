import pytest
import httpx
from http import HTTPStatus

from unittest.mock import AsyncMock
from unittest.mock import MagicMock

from app.core.init_app import init_controllers

from app.main import app as app_

@pytest.fixture
async def app():
    app_.db = MagicMock()
    app_.alarm_repository = AsyncMock()
    await init_controllers(app_)
    return app_


@pytest.fixture
async def test_client(app):
    async with httpx.AsyncClient(app=app, base_url="http://testserver") as client:
        yield client

@pytest.mark.asyncio
async def test_get_config(test_client):
    response = await test_client.get("/v1/alarm/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "currentSetTime": "10:01",
        "isAlarmOn": True,
    }

@pytest.mark.asyncio
async def test_post_config(test_client):
    response = await test_client.post("/v1/alarm/", json={"active": "False", "time": "10:00"})
    assert response.status_code == HTTPStatus.OK
    assert response.text == "true"
