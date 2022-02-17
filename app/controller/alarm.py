from datetime import datetime
import logging
from random import randrange


from fastapi import Request
from app.entities.alarm import AlarmConfig, AlarmConfigBase

from app.repository.alarm import AlarmRepository

logger = logging.getLogger(__name__)

class AlarmController():
    alarm_repository: AlarmRepository

    def __init__(self, alarm_repository: AlarmRepository):
        self.alarm_repository = alarm_repository
    
    async def update(self, config: AlarmConfigBase) -> AlarmConfig:
      new_config = AlarmConfig(time=config.time, active=config.active, id=1, timestamp=datetime.now())
      existing_config = await self.alarm_repository.get(alarm_id=1)
      if existing_config is None:
        await self.alarm_repository.create(new_config)
      else:
        await self.alarm_repository.update(new_config)
      return new_config
      
    async def get(self) -> AlarmConfig:
      return await self.alarm_repository.get(alarm_id=1)