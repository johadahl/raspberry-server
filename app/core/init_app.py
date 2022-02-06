from app.controller.alarm import AlarmController
from app.repository.alarm import AlarmRepository

async def init_repositories(app):
  app.alarm_repository = AlarmRepository(db=app.db)

async def init_controllers(app):
  app.alarm_controller = AlarmController(alarm_repository=app.alarm_repository)