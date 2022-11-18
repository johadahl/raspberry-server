import logging
from dataclasses import dataclass

import redis

logger = logging.getLogger(__name__)

@dataclass
class RedisRepository:
    connection: redis.Redis

    def __init__(self, url: str): 
        self.connection = redis.Redis(url)

    async def disconnect(self):
        self.connection.disconnect()

    def set_active(self):
        self.connection.set('active', 1)

    def set_inactive(self):
        self.connection.set('active', 0)

