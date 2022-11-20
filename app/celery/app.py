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

async def test():
    db = AlarmRepository(db=await db_connect())
    config = await db.get(settings.DEFAULT_ALARM_ID)
    print("job started, config: ", config.dict())
    if config is None or config.is_snoozed: return

    while not config.is_snoozed:
        print("ring ring!")
        sleep(3)
        config = await db.get(settings.DEFAULT_ALARM_ID)
        print("latest config: ", config)


@app.task
def ring_bell():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())

@app.task
async def reset_snooze():
    db = AlarmRepository(db=await db_connect())
    await db.set_snooze(False)