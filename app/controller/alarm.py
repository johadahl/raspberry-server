import logging
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler

from app.entities.alarm import AlarmConfig, AlarmConfigBase
from app.repository.alarm import AlarmRepository
from app.utils.scheduler import set_schedule

logger = logging.getLogger(__name__)

DEFAULT_ALARM_ID = 1
class AlarmController:
    alarm_repository: AlarmRepository
    scheduler: BackgroundScheduler

    def __init__(
        self, alarm_repository: AlarmRepository, scheduler: BackgroundScheduler
    ):
        self.alarm_repository = alarm_repository
        self.scheduler = scheduler

    async def update(self, config: AlarmConfig) -> AlarmConfig:
        new_config = AlarmConfig(
            time=config.time, active=config.active, id=DEFAULT_ALARM_ID, timestamp=datetime.now()
        )
        existing_config = await self.alarm_repository.get(alarm_id=DEFAULT_ALARM_ID)
        if existing_config is None:
            await self.alarm_repository.create(new_config)
        else:
            await self.alarm_repository.update(new_config)
        set_schedule(config=new_config, scheduler=self.scheduler)
        return new_config

    async def get(self) -> AlarmConfig:
        return await self.alarm_repository.get(alarm_id=1)
