from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from app import settings
from app.entities.alarm import AlarmConfig
from app.utils.servo import ring_bell

def set_schedule(config: AlarmConfig, scheduler: BackgroundScheduler):
    job = scheduler.get_job(settings.CRON_ID)
    trigger = CronTrigger(
        hour=config.time.split(":")[0], 
        minute=config.time.split(":")[1],
        timezone='Europe/Berlin'
    )

    if config.active:
        if job is None:
            scheduler.add_job(ring_bell, trigger, id=settings.CRON_ID)
        else:
            job.reschedule(trigger)
        return

    if job is not None:
        scheduler.remove_job(settings.CRON_ID)
