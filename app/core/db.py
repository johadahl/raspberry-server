import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import settings
from app.repository import models

logger = logging.getLogger(__name__)


async def boot(app):
    try:
        engine = create_engine(
            settings.DATABASE_URL, connect_args={"check_same_thread": False}
        )

        models.Base.metadata.create_all(bind=engine)

        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

        app.db = SessionLocal()

    except Exception as exc:
        logger.critical(
            "Unknown error occurred while trying to establish to database connection",
            exc_info=exc,
        )
