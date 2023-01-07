from fastapi import APIRouter, Depends, Path, Query
from ..iam.base_schemas import AccessType, ResponseCollection
from ..schedule.schemas.session import SessionCreateModel
from ..schedule.schemas.bookings import BookingsCreateModel
from ..iam.schemas.merchant import MerchantCreateModel
from ..iam.schemas.merchant import MerchantModel
from ..iam.schemas.auth import AuthModel, AuthResponse
from ..schedule import service


studio_router = APIRouter(
    prefix="/studios",
    tags=["Schedule"],
    responses={404: {"message": "Not Found | 404"}},
)


bookings_router = APIRouter(
    prefix="/bookings",
    tags=["Schedule"],
    responses={404: {"message": "Not Found | 404"}},
)


@studio_router.get("/{merchant_id}")
def fetch_studio_sessions(merchant_id: str):
    return service.fetch_studio_sessions(merchant_id)


@studio_router.post("/{merchantId}")
def create_studio_session(merchantId: str, session: SessionCreateModel):
    return service.create_studio_session(session, merchantId)


@bookings_router.post("/")
def create_studio_session(booking: BookingsCreateModel):
    return service.book_session(booking)
