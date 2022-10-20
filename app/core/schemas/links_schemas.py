import datetime

from pydantic import BaseModel


class CreateLinkModel(BaseModel):
    link: str
    live_interval: int


class ResponseLinkModel(BaseModel):
    id: int
    link: str
    short_link: str
    live_interval: datetime.timedelta

    class Config:
        orm_mode = True
