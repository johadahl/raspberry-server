import logging
from typing import Union
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.entities.alarm import AlarmConfig
from app.repository.models import AlarmConfig as AlarmModel

logger = logging.getLogger(__name__)


class AlarmRepository:
    _db: Session

    def __init__(self, db: Session):
        self._db = db

    async def get(self, alarm_id: int) -> Union[AlarmConfig,None]:
        statement = select(AlarmModel).filter_by(id=alarm_id)
        res = self._db.execute(statement).scalars().first()
        return AlarmConfig(
            id=res.id,
            timestamp=res.timestamp,
            time=res.time,
            active=res.active,
            day_of_week=res.day_of_week,
            is_snoozed=res.is_snoozed,
            snooze_interval=res.snooze_interval
        ) if res else None

    async def create(self, config: AlarmConfig) -> AlarmConfig:
        db_alarm_config = AlarmModel(**config.dict())
        self._db.add(db_alarm_config)
        self._db.commit()
        self._db.refresh(db_alarm_config)
        return config

    async def update(self, config: AlarmConfig) -> AlarmConfig:
        x = self._db.query(AlarmModel).get(config.id)
        x.time = config.time
        x.active = config.active
        x.timestamp = config.timestamp
        x.is_snoozed = config.is_snoozed
        x.snooze_interval = config.snooze_interval
        x.day_of_week = config.day_of_week
        self._db.commit()
        return config
