import logging
from sqlalchemy.orm import Session

from app.repository import models
from app.entities.alarm  import AlarmConfig, AlarmConfigBase

logger = logging.getLogger(__name__)

class AlarmRepository():
    _db: Session

    def __init__(self, db: Session):
        self._db = db

    async def get_alarm(self, alarm_id: int):
        return self._db.query(AlarmConfig).filter(AlarmConfig.id == alarm_id).first()

    async def create_alarm(self, alarm_config: AlarmConfig):
        db_alarm_config = models.AlarmConfig(**alarm_config.dict())
        self._db.add(db_alarm_config)
        self._db.commit()
        self._db.refresh(db_alarm_config)
        return True
