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

def set_snooze(scheduler: AsyncIOScheduler, interval: int):
    snooze_job = scheduler.get_job(settings.CRON_SNOOZE_ID)
    alarm_job = scheduler.get_job(settings.CRON_ALARM_ID)
    
    # next_alarm = (datetime.now() + timedelta(minutes=interval)).minute
    next_alarm = (datetime.now() + timedelta(minutes=1)).minute
    
    alarm_trigger = CronTrigger(minute=next_alarm, timezone='Europe/Berlin')
    snooze_trigger = CronTrigger(minute=next_alarm-1, timezone='Europe/Berlin')

    if snooze_job is None:
        scheduler.add_job(delay_snooze, snooze_trigger, id=settings.CRON_SNOOZE_ID)
        return
    if alarm_job is None:
        scheduler.add_job(delay_alarm, alarm_trigger, id=settings.CRON_ALARM_ID)
        return
    
    snooze_job.reschedule(snooze_trigger)
    snooze_job.reschedule(alarm_trigger)

def set_schedule(config: AlarmConfig, scheduler: AsyncIOScheduler):
    job = scheduler.get_job(settings.CRON_ALARM_ID)
    trigger = CronTrigger(
        # hour="{}-23".format(config.time.split(":")[0]), 
        # minute="{}-59".format(config.time.split(":")[1]),
        hour=config.time.split(":")[0], 
        minute=config.time.split(":")[1],
        timezone='Europe/Berlin'
    )
    if config.active:
        if job is None:
            scheduler.add_job(delay_alarm, trigger, id=settings.CRON_ALARM_ID)
        else:
            job.reschedule(trigger)
        return

    if job is not None:
        scheduler.remove_job(settings.CRON_ALARM_ID)


