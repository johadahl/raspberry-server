from __future__ import annotations
import os

from fastapi import APIRouter, Depends, Request, Response

from app.controller.alarm.get_config import get_config
from app.controller.alarm.set_config import set_config
from app.controller.alarm.set_config import AlarmConfig
from app.core.auth import get_current_user


router = APIRouter()

admin_html = os.path.join(os.path.dirname(__file__), 'templates', 'admin.html')

@router.get("/alarm/", tags=["alarm"])
async def get_alarm_config(
    # auth: Depends = Depends(get_current_user),    // TODO: fix auth flow
) -> dict[str, int]:
    return get_config()

@router.post("/alarm/", tags=["alarm"])
async def set_alarm_config(
    config: AlarmConfig,
    # auth: Depends = Depends(get_current_user),    // TODO: fix auth flow
) -> dict[str, int]:
    return set_config(config)
