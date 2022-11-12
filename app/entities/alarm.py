from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class AlarmConfigBase(BaseModel):
    time: str
    active: bool
    day_of_week: Optional[str] # "mon,tue,wed,thu,fri,sat,sun"
    is_snoozed: Optional[bool]
    snooze_interval: Optional[int]

class AlarmConfig(AlarmConfigBase):
    id: int
    timestamp: datetime
