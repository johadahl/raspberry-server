from app.controller.alarm import AlarmController
from app.repository.alarm import AlarmRepository
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from app import settings

def init_repositories(app):
  app.alarm_repository = AlarmRepository(db=app.db)

def init_controllers(app):
  app.alarm_controller = AlarmController(alarm_repository=app.alarm_repository)

def some_job():
  print("Hello World")

async def init_scheduler(app):
  scheduler = BackgroundScheduler()
  current_setting = await app.alarm_repository.get(alarm_id=1)

  if current_setting.active:
    trigger = CronTrigger(hour=current_setting.time.split(":")[0], minute=current_setting.time.split(":")[1])
    scheduler.add_job(some_job, trigger, id=settings.CRON_ID)
  scheduler.start()
  app.scheduler = scheduler