from __future__ import annotations
import os

from fastapi import APIRouter, Depends, Request, Response

from app.apis.alarm.get_config import get_config
from app.apis.alarm.set_config import set_config
from app.core.auth import get_current_user

router = APIRouter()

admin_html = os.path.join(os.path.dirname(__file__), 'templates', 'admin.html')

@router.get("/v1/alarm/", tags=["alarm"])
async def get_alarm_config(
    # auth: Depends = Depends(get_current_user),    // TODO: fix auth flow
) -> dict[str, int]:
    return get_config()

@router.post("/v1/alarm/", tags=["alarm"])
async def set_alarm_config(
    # auth: Depends = Depends(get_current_user),    // TODO: fix auth flow
) -> dict[str, int]:
    return set_config()


@router.get(
    path='/',
    description='The Admin Panel',
)
async def get_admin(
    request: Request,
    # auth: Depends = Depends(get_current_user),
):
    with open(admin_html, 'r') as fh:
        return Response(content=fh.read())
