import asyncio
from app.core.db import db_connect
from app.repository.alarm import AlarmRepository
from celery import Celery
from app import settings
from time import sleep

app = Celery('tasks', broker=settings.REDIS_URI)

app.conf.update(
    timezone=settings.TZ_INFO,
)

def async_task(fun, **opts):
    def run_sync(*args, **kwargs):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(fun(*args, **kwargs))

    task = app.task(
        run_sync,
        name='.'.join([fun.__module__, fun.__name__]) if fun.__name__ != 'run' else fun.__module__,
        **opts,
    )

    task.run_async = fun

    return task

@async_task
async def ring_bell():
    print("Ring alarm task")
    db = AlarmRepository(db=await db_connect())
    config = await db.get(settings.DEFAULT_ALARM_ID)
    if config is None or config.is_snoozed: return

    while not config.is_snoozed:
        print("ring ring!")
        sleep(3)
        config = await db.get(settings.DEFAULT_ALARM_ID)

@async_task
async def reset_snooze():
    print("Reset snooze task")
    db = AlarmRepository(db=await db_connect())
    await db.set_snooze(False)