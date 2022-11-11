from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from app import settings
from app.entities.alarm import AlarmConfig
from app.utils.servo import ring_bell

SNOOZE = 2 # minutes

def set_schedule(config: AlarmConfig, scheduler: BackgroundScheduler):
    job = scheduler.get_job(settings.CRON_ID)
    trigger = CronTrigger(
        hour=str(config.time.split(":")[0], + "-23"), 
        minute=str(config.time.split(":")[1], + "-59/" + SNOOZE),
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
