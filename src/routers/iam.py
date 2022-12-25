from fastapi import APIRouter
from ..iam.schemas import user, merchant
from ..iam import service

register_router = APIRouter(
    prefix="/register",
    tags=["register"],
    responses={404: {"message": "Not Found | 404"}},
)

sign_in_router = APIRouter(
    prefix="/sign-in",
    tags=["sign_in"],
    responses={404: {"message": "Not Found | 404"}},
)

@register_router.post("/users")
def register_user(user: user.UserCreateModel):
    return service.register_user(user)

@register_router.post("/merchants")
def register_merchant(merchant: merchant.MerchantCreateModel):
    return service.register_merchant(merchant)

@sign_in_router.get("/")
def register_merchant():
    pass