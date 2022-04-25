from __future__ import annotations

import os
import re

from fastapi import APIRouter, Depends, Request, Response

from app.core.auth import get_current_user
from app.entities.alarm import AlarmConfig

router = APIRouter()

admin_html = os.path.join(os.path.dirname(__file__), "templates", "admin.html")


@router.get("/alarm/", tags=["alarm"])
async def get_alarm_config(
    request: Request,
    # auth: Depends = Depends(get_current_user),    // TODO: fix auth flow
) -> dict[str, int]:
    res = await request.app.alarm_controller.get()
    return res


@router.post("/alarm/", tags=["alarm"])
async def set_alarm_config(
    request: Request,
    config: AlarmConfig,
    # auth: Depends = Depends(get_current_user),    // TODO: fix auth flow
) -> dict[str, int]:
    return await request.app.alarm_controller.update(config)
