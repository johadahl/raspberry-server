from datetime import datetime
import logging
from random import randrange


from fastapi import Request
from app.entities.alarm import AlarmConfig, AlarmConfigBase

from app.repository.alarm import AlarmRepository
from apscheduler.schedulers.background import BackgroundScheduler
from app.utils.scheduler import set_schedule

logger = logging.getLogger(__name__)

class AlarmController():
    alarm_repository: AlarmRepository
    scheduler: BackgroundScheduler

    def __init__(self, alarm_repository: AlarmRepository, scheduler: BackgroundScheduler):
        self.alarm_repository = alarm_repository
        self.scheduler = scheduler
    
    async def update(self, config: AlarmConfigBase) -> AlarmConfig:
      new_config = AlarmConfig(time=config.time, active=config.active, id=1, timestamp=datetime.now())
      existing_config = await self.alarm_repository.get(alarm_id=1)
      if existing_config is None:
        await self.alarm_repository.create(new_config)
      else:
        await self.alarm_repository.update(new_config)
      set_schedule(config=new_config, scheduler=self.scheduler)
      return new_config
      
    async def get(self) -> AlarmConfig:
      return await self.alarm_repository.get(alarm_id=1)