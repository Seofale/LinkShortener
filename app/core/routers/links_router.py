import datetime
import validators

from fastapi import APIRouter, Path, HTTPException
from fastapi.requests import Request

from core.utils.links_utils import generate_link
from core.schemas.links_schemas import CreateLinkModel, ResponseLinkModel
from core.models.links_models import Links


links_router = APIRouter(prefix='/links', tags=['links'])


def not_valid_url():
    message = 'This URL is not valid'
    raise HTTPException(status_code=400, detail=message)


def url_not_fount(request: Request):
    message = f'URL {request.url} not found'
    raise HTTPException(status_code=404, detail=message)


@links_router.post('/', status_code=201, response_model=ResponseLinkModel)
async def create_shortener_link(body: CreateLinkModel):
    if not validators.url(body.link):
        return not_valid_url()

    short_link = generate_link()
    link_id = await Links.create(
        link=body.link,
        short_link=short_link,
        live_interval=datetime.timedelta(days=body.live_interval)
    )

    return ResponseLinkModel(**body.dict(), id=link_id, short_link=short_link)


@links_router.get('/{short_link}', status_code=200, response_model=ResponseLinkModel)
async def get_link_by_shortener_link(
    request: Request,
    short_link: str = Path(title='Short link to get full')
):
    link = await Links.get_full_link_by_short_link(short_link)

    if not link:
        return url_not_fount(request)

    return ResponseLinkModel(**link)
