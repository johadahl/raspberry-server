from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AlarmConfig(Base):
    __tablename__ = "alarms"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, index=True)
    time = Column(String)
    active = Column(Boolean)
    is_snoozed = Column(Boolean)
    snooze_interval = Column(Integer)
    day_of_week = Column(String)
