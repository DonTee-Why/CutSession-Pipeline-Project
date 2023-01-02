from fastapi import APIRouter, Depends, Path, Query
from ..iam.base_schemas import AccessType, ResponseCollection
from ..iam.schemas.user import UserCreateModel
from ..iam.schemas.merchant import MerchantCreateModel
from ..iam.schemas.auth import AuthModel, AuthResponse
from ..iam import service

register_router = APIRouter(
    prefix="/register",
    tags=["register"],
    responses={404: {"message": "Not Found | 404"}},
)

sign_in_router = APIRouter(
    prefix="/sign-in",
    tags=["sign_in"],
)

clients_router = APIRouter(
    prefix="/clients",
    tags=["clients"],
)

@register_router.post("/users")
def register_user(user: UserCreateModel):
    return service.register_user(user)

@register_router.post("/merchants")
def register_merchant(merchant: MerchantCreateModel):
    return service.register_merchant(merchant)

@sign_in_router.post("/", response_model=AuthResponse, response_model_exclude_none=True)
async def login(user: AuthModel):
    return await service.authorize(user)

@clients_router.post("/", response_model=ResponseCollection, response_model_exclude_none=True)
async def fetch_clients(limit: int, offset: int, type: AccessType, city: str = "", name: str = ""):
    return await service.fetch_clients(limit, offset, type, city, name)