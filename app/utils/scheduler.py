from datetime import datetime, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from app.celery.app import ring_bell, reset_snooze
from app.entities.alarm import AlarmConfig
from app import settings

async def delay_alarm():
    ring_bell.delay()

async def delay_snooze():
    reset_snooze.delay()

def set_snooze_schedule(scheduler: AsyncIOScheduler, interval: int):
    scheduler.remove_all_jobs()
    
    next = (datetime.now() + timedelta(minutes=interval)).minute
    # next = (datetime.now() + timedelta(minutes=2)).minute # For testing
    
    alarm_trigger = CronTrigger(minute=next, timezone='Europe/Berlin')
    snooze_trigger = CronTrigger(minute=next-1, timezone='Europe/Berlin')

    scheduler.add_job(delay_snooze, snooze_trigger, id=settings.CRON_SNOOZE_ID)
    scheduler.add_job(delay_alarm, alarm_trigger, id=settings.CRON_ALARM_ID)
    
def reset_schedule(config: AlarmConfig, scheduler: AsyncIOScheduler):
    scheduler.remove_all_jobs()
    if not config.active: return

    # set alarm trigger:
    trigger = CronTrigger(
        # hour="{}-23".format(config.time.split(":")[0]), 
        # minute="{}-59".format(config.time.split(":")[1]),
        hour=config.time.split(":")[0], 
        minute=config.time.split(":")[1],
        timezone='Europe/Berlin'
    ) 
    scheduler.add_job(delay_alarm, trigger, id=settings.CRON_ALARM_ID)
    scheduler.add_job(
        delay_snooze, 
        next_run_time=datetime.now(tz=settings.TZ)+timedelta(minutes=1), 
        id=settings.CRON_SNOOZE_ID
        )
