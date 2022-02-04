from __future__ import annotations

import os

from fastapi import APIRouter, Response

from app.core.auth import get_current_user

router = APIRouter()

admin_html = os.path.join(os.path.dirname(__file__), "../templates/admin.html")


@router.get(path="/", tags=["alarm"])
async def get_admin():
    with open(admin_html, "r") as fh:
        return Response(content=fh.read())


# TODO: Add login and logout
