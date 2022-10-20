from sqlalchemy import create_engine
import databases

from config import settings


database = databases.Database(settings.DATABASE_URL)

engine = create_engine(settings.DATABASE_URL, echo=True)
