from celery import Celery
from app import settings
from time import sleep

app = Celery('tasks', broker=settings.REDIS_URI)


@app.task
async def ring_bell():
    print("ring ring!")
    sleep(10)
    return True