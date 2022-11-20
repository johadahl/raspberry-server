from typing import Union
import logging
from datetime import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.entities.alarm import AlarmConfig
from app.repository.alarm import AlarmRepository
from app.utils.scheduler import set_schedule, set_snooze
from app import settings

logger = logging.getLogger(__name__)

class AlarmController:
    alarm_repository: AlarmRepository
    scheduler: AsyncIOScheduler

    def __init__(
        self, 
        alarm_repository: AlarmRepository, 
        scheduler: AsyncIOScheduler,
    ):
        self.alarm_repository = alarm_repository
        self.scheduler = scheduler

    async def update(self, config: AlarmConfig) -> AlarmConfig:
        new_config = AlarmConfig(
            id=settings.DEFAULT_ALARM_ID, 
            timestamp=datetime.now(tz=settings.TZ),
            time=config.time, 
            active=config.active, 
            day_of_week=config.day_of_week,
            is_snoozed=config.is_snoozed,
            snooze_interval=config.snooze_interval
        )
        existing_config = await self.alarm_repository.get(alarm_id=settings.DEFAULT_ALARM_ID)
        if existing_config is None:
            await self.alarm_repository.create(new_config)
        else:
            await self.alarm_repository.update(new_config)
        set_schedule(config=new_config, scheduler=self.scheduler)
        return new_config

    async def get(self) -> Union[AlarmConfig, None]:
        return await self.alarm_repository.get(alarm_id=settings.DEFAULT_ALARM_ID)

    async def snooze(self, state: bool, id: int = settings.DEFAULT_ALARM_ID) -> Union[AlarmConfig, None]:        
        await self.alarm_repository.set_snooze(state)
        config = await self.alarm_repository.get(alarm_id=id)
        print("UPDATED CONFIG: ", config)
        # if config is None or config.is_snoozed == state: return
        

        # if state == False: return state 

        # set_snooze(self.scheduler, config.snooze_interval)

        return state

    async def reset(self, state: bool, id: int = settings.DEFAULT_ALARM_ID) -> Union[AlarmConfig, None]:
        config = await self.alarm_repository.get(alarm_id=id)
        self.alarm_repository.set_snooze(True)
        # TODO: Set is_snoozed 1 minute later
        set_schedule(config=config, scheduler=self.scheduler)
        return config