# TODO: Clean this up and make it relevant

from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_get_config():
    response = client.get("/v1/alarm")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "currentSetTime": "10:01",
        "isAlarmOn": True,
    }

