from time import sleep
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from app.core.db import db_connect
from app.repository.alarm import AlarmRepository
from app.entities.alarm import AlarmConfig
from app import settings

async def alarm_trigger():
    db = AlarmRepository(db=await db_connect())
    current_alarm = await db.get(alarm_id=settings.DEFAULT_ALARM_ID)
    if current_alarm is None or current_alarm.is_snoozed: return
    
    print("alarm triggered: ", current_alarm.dict())
    # ring_once()
    sleep(10)
    print("Ring ring")
    return

def set_schedule(config: AlarmConfig, scheduler: AsyncIOScheduler):
    job = scheduler.get_job(settings.CRON_ID)
    trigger = CronTrigger(
        hour=config.time.split(":")[0], 
        # minute="{}-59/{}".format(config.time.split(":")[1], config.snooze_interval),
        minute=config.time.split(":")[1],
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
