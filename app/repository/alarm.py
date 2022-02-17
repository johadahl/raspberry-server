import logging
from sqlalchemy.orm import Session
from sqlalchemy import select


from app.repository.models import AlarmConfig as AlarmModel
from app.entities.alarm  import AlarmConfig

logger = logging.getLogger(__name__)

class AlarmRepository():
    _db: Session

    def __init__(self, db: Session):
        self._db = db

    async def get(self, alarm_id: int):
        statement = select(AlarmModel).filter_by(id=alarm_id)
        res = self._db.execute(statement).scalars().first()        
        return res

    async def create(self, config: AlarmConfig):
        db_alarm_config = AlarmModel(**config.dict())
        self._db.add(db_alarm_config)
        self._db.commit()
        self._db.refresh(db_alarm_config)
        return config

    async def update(self, config: AlarmConfig):
        x =  self._db.query(AlarmModel).get(config.id)
        x.time = config.time
        x.active = config.active
        x.timestamp = config.timestamp
        self._db.commit()
        return config