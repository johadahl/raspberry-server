from __future__ import annotations

import os
import re

from fastapi import APIRouter, Depends, Request, Response

from app.core.auth import get_current_user
from app.entities.alarm import AlarmConfigBase

router = APIRouter()

admin_html = os.path.join(os.path.dirname(__file__), "templates", "admin.html")


@router.get("/alarm/", tags=["alarm"])
async def get_alarm_config(
    request: Request,
    # auth: Depends = Depends(get_current_user),    // TODO: fix auth flow
) -> dict[str, int]:
    return await request.app.alarm_controller.get()


@router.post("/alarm/", tags=["alarm"])
async def set_alarm_config(
    request: Request,
    config: AlarmConfigBase,
    # auth: Depends = Depends(get_current_user),    // TODO: fix auth flow
) -> dict[str, int]:
    return await request.app.alarm_controller.create(config)
