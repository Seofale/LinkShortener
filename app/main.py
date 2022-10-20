from fastapi import FastAPI

from config import settings
from core.routers.links_router import links_router
from database.engine import database, engine
from core.models.links_models import Links


def create_tables():
    Links.metadata.create_all(engine)


def include_routers(app):
    app.include_router(links_router)


def get_application():
    create_tables()
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_routers(app)
    return app


app = get_application()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
