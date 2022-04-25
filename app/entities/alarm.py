from datetime import datetime

from pydantic import BaseModel


class AlarmConfigBase(BaseModel):
    time: str
    active: bool


class AlarmConfig(AlarmConfigBase):
    id: int
    timestamp: datetime
