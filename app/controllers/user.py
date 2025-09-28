from fastapi import APIRouter, Depends
from ..services.user_service import UserService
from ..utils.service_factory import service_factory

from ..schemas import user_schema

router = APIRouter(prefix="/user", tags=["user"])

@router.post("/")
async def create_user(
    user: user_schema.UserCreate,
    service: UserService = Depends(service_factory(UserService))
): 
    return await service.create_user(user)

@router.get("/{user_id}")
async def get_user(
    user_id: str,
    service: UserService = Depends(service_factory(UserService))
):
    return await service.get_user_by_id(user_id)

@router.get("/", response_model=list[user_schema.UserOut])
async def get_all_user(
    service: UserService = Depends(service_factory(UserService))
):
    return await service.get_all_users()

