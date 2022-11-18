"""
Settings
"""

from os import getenv
from pytz import timezone

TITLE = "Rasperry Pi Server"

ENVIRONMENT = getenv("APP_ENVIRONMENT")
RELEASE = getenv("GIT_HASH_SHORT", "NONE")

PORT = int(getenv("PORT", "8080"))
HOST = getenv("HOST")
DEBUG = getenv("DEBUG") == "1"

DATABASE_URL = getenv("DATABASE_URL")
DATABASE_NAME = getenv("DATABASE_NAME")

CRON_ID = getenv("CRON_ID", "1")

DEFAULT_ALARM_ID = 1

REDIS_URI = getenv("REDIS_URI", "redis://redis:6379")

TZ_INFO = 'Europe/Berlin'
TZ = timezone(TZ_INFO)
