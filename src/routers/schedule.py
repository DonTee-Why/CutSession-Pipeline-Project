from fastapi import APIRouter, Depends, Path, Query
from ..iam.base_schemas import AccessType, ResponseCollection
from ..schedule.schemas.session import SessionCreateModel
from ..iam.schemas.merchant import MerchantCreateModel
from ..iam.schemas.merchant import MerchantModel
from ..iam.schemas.auth import AuthModel, AuthResponse
from ..schedule import service


studio_router = APIRouter(
    prefix="/studios",
    tags=["schedule"],
    responses={404: {"message": "Not Found | 404"}},
)


# @studio_router.get("/{merchant_id}")
# def fetch_studio_sessions(merchant_id: str = Depends(service.get_merchant_by_id)):
#     return service.fetch_studio_sessions(merchant_id)


@studio_router.post("/{merchantId}")
def create_studio_session(merchantId: str, session: SessionCreateModel ):
    return service.create_studio_session(session, merchantId)


# @bookings_router.get("/", response_model=AuthResponse, response_model_exclude_none=True)
# async def login(user: AuthModel):
#     return await service.authorize(user)


# @bookings_router.post("/", response_model=ResponseCollection, response_model_exclude_none=True)
# async def fetch_clients(limit: int, offset: int, type: AccessType, city: str = "", name: str = ""):
#     return await service.fetch_clients(limit, offset, type, city, name)
