from datetime import datetime, timedelta
from time import sleep
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from app.core.db import db_connect
from app.entities.alarm import AlarmConfig
from app import settings

async def alarm_trigger():
    # Redis -> alarm_on:True
    print("Ring ring")
    sleep(5)

def set_schedule(config: AlarmConfig, scheduler: AsyncIOScheduler):
    job = scheduler.get_job(settings.CRON_ID)
    trigger = CronTrigger(
        hour="{}-23".format(config.time.split(":")[0]), 
        # hour=config.time.split(":")[0], 
        minute="{}-59".format(config.time.split(":")[1]),
        # minute=config.time.split(":")[1],
        timezone='Europe/Berlin'
    )

    if config.active:
        if job is None:
            scheduler.add_job(alarm_trigger, trigger, id=settings.CRON_ID)
        else:
            job.reschedule(trigger)
        return

    if job is not None:
        scheduler.remove_job(settings.CRON_ID)


def snooze(config: AlarmConfig, scheduler: AsyncIOScheduler):
    job = scheduler.get_job(settings.CRON_ID)
    new_trigger = CronTrigger(
        hour=datetime.now(tz=settings.TZ).hour, 
        minute=(datetime.now(tz=settings.TZ) + timedelta(minutes=5)).minute,
        timezone='Europe/Berlin'
    )
    job.reschedule(new_trigger)
    # redis -> alarm_on:False
