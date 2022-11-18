import logging
from dataclasses import dataclass
from dataclasses import field

import aioredis

logger = logging.getLogger(__name__)

@dataclass
class Redis:
    url: str
    pool: aioredis.commands.Redis = field(default=None, init=False)

    async def init(self):
        self.pool = await aioredis.create_redis_pool(address=self.url)
        logger.info('Redis connection succeeded')

    async def shutdown(self):
        self.pool.close()
        await self.pool.wait_closed()

    async def set_active(self):
        await self.pool.set(key=f'active', value=True)

    async def set_inactive(self):
        await self.pool.set(key=f'active', value=False)

