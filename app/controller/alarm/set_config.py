from __future__ import annotations
from pydantic import BaseModel

class AlarmConfig(BaseModel):
    time: str
    active: bool

def set_config(config: AlarmConfig) -> bool:
    return True