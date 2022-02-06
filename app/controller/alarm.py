import logging

from fastapi import Request
from app.entities.alarm import AlarmConfigBase

from app.repository.alarm import AlarmRepository

logger = logging.getLogger(__name__)

class AlarmController():
    alarm_repository: AlarmRepository

    def __init__(self, alarm_repository: AlarmRepository):
        self.alarm_repository = alarm_repository

    async def create(self, config: AlarmConfigBase) -> bool:
      print("Save config: ", config)
      # TODO; store to in DB
      return True 
    
    async def get(self) -> bool:
      return {
        "currentSetTime": "10:01",
        "isAlarmOn": True,
    }  