import datetime

from sqlalchemy import Column, Integer, String, Date, Interval

from core.models.base_model import Base
from database.engine import database


class Links(Base):
    id = Column(Integer, primary_key=True)
    link = Column(String(100))
    short_link = Column(String(20))
    created_date = Column(Date())
    live_interval = Column(Interval(day_precision=True))

    def __str__(self):
        return f'({self.id}) {self.title}'

    @classmethod
    async def create(
            cls,
            link: str,
            short_link: str,
            live_interval: datetime.timedelta,
            created_date=datetime.date.today()
    ):
        query = cls.__table__.insert().values(
            link=link,
            short_link=short_link,
            live_interval=live_interval,
            created_date=created_date
        )

        return await database.execute(query)

    @classmethod
    async def get_full_link_by_short_link(cls, short_link: str):
        query = cls.__table__.select().filter(cls.__table__.c.short_link==short_link)

        return await database.fetch_one(query)

    @classmethod
    async def get_all_links(cls):
        query = cls.__table__.select()
        database_objects = await database.fetch_all(query)
        links = [dict(database_object) for database_object in database_objects]

        return links
