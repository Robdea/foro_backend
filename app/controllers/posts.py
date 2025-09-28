from fastapi import APIRouter, Depends

from ..services.posts_services import PostService
from ..utils.service_factory import service_factory

from ..schemas import posts_schemas
from ..utils.auth import get_current_user

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("/", response_model=list[posts_schemas.PostOut])
async def get_all(
    service: PostService =  Depends(service_factory(PostService))
):
    return await service.get_all_post()


@router.post("/")
async def create_post(
    post: posts_schemas.PostCreate,
    service: PostService =  Depends(service_factory(PostService)),
    current_user: dict = Depends(get_current_user)
):
    return await service.create_post(post, author_id=current_user["id"])
