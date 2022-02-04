from __future__ import annotations

import os

from fastapi import APIRouter, Depends, Request, Response

from app.controller.alarm.get_config import get_config
from app.controller.alarm.set_config import AlarmConfig, set_config
from app.core.auth import get_current_user

router = APIRouter()

admin_html = os.path.join(os.path.dirname(__file__), "../templates/admin.html")


@router.get(path="/", tags=["alarm"])
async def get_admin():
    with open(admin_html, "r") as fh:
        return Response(content=fh.read())


# TODO: Add login and logout
