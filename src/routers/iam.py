from fastapi import APIRouter, Depends
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

@register_router.post("/users")
def register_user(user: UserCreateModel):
    return service.register_user(user)

@register_router.post("/merchants")
def register_merchant(merchant: MerchantCreateModel):
    return service.register_merchant(merchant)

@sign_in_router.post("/", response_model=AuthResponse, response_model_exclude_none=True)
async def login(user: AuthModel):
    return await service.authorize(user)