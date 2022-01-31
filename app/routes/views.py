from __future__ import annotations
import os

from fastapi import APIRouter, Depends, Request, Response

from app.apis.api_a.mainmod import main_func as main_func_a
from app.apis.api_b.mainmod import main_func as main_func_b
from app.core.auth import get_current_user

router = APIRouter()

admin_html = os.path.join(os.path.dirname(__file__), 'templates', 'admin.html')

@router.get("/api_a/{num}", tags=["api_a"])
async def view_a(
    num: int,
    auth: Depends = Depends(get_current_user),
) -> dict[str, int]:
    return main_func_a(num)


@router.get("/api_b/{num}", tags=["api_b"])
async def view_b(
    num: int,
    auth: Depends = Depends(get_current_user),
) -> dict[str, int]:
    return main_func_b(num)

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
