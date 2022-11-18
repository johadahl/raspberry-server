from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.controller.alarm import AlarmController
from app.repository.alarm import AlarmRepository
from app.repository.redis import RedisRepository
from app.utils.scheduler import set_schedule
from app import settings

def init_repositories(app):
    app.alarm_repository = AlarmRepository(db=app.db)


async def init_scheduler(app):
    scheduler = AsyncIOScheduler()
    config = await app.alarm_repository.get(alarm_id=1)
    if config: set_schedule(config, scheduler)
    scheduler.start()
    app.scheduler = scheduler

def init_redis(app):
    app.redis = RedisRepository(url=settings.REDIS_URI)

def init_controllers(app):
    app.alarm_controller = AlarmController(
        alarm_repository=app.alarm_repository, 
        scheduler=app.scheduler,
        redis=app.redis,
    )
