from app.entities.alarm import AlarmConfig
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from app import settings

def some_job():
    print("Hello World!")

def set_schedule(config: AlarmConfig, scheduler: BackgroundScheduler):
    job = scheduler.get_job(settings.CRON_ID)
    trigger = CronTrigger(hour=config.time.split(":")[0], minute=config.time.split(":")[1])

    if config.active:
      if job is None:
        scheduler.add_job(some_job, trigger, id=settings.CRON_ID)
      else:        
        job.reschedule(trigger)
      return

    if job is not None:
      scheduler.remove_job(settings.CRON_ID)