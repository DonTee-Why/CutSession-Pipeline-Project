from datetime import datetime, timedelta
from fastapi import HTTPException, status, Security, Depends, Request
from ..config import AppSettings
from .base_schemas import AccessType, ResponseCollection
from ..iam.schemas.user import UserCreateModel, UserModel, UserInModel
from ..iam.schemas.merchant import MerchantModel, MerchantInModel
from .schemas.session import SessionCreateModel, SessionModel
from .schemas.bookings import BookingsCreateModel, BookingsModel
from ..database.database import DBManager, User, Merchant, Session, Booking
from .booking_ref import BookingRef, DerivedStrategy


db = DBManager()
user = User()
merchant = Merchant()
session = Session()
booking = Booking()
settings = AppSettings()


def get_merchant_by_id(id: str) -> MerchantModel:
    merchant_query = merchant.select().where("merchant_id", "=", id)
    data = db.fetch_one(merchant_query.query)

    if data is None:
        return None

    return MerchantModel(**data)


def get_session_by_id(id: str) -> SessionModel:
    session_query = session.select().where("session_id", "=", id)
    data = db.fetch_one(session_query.query)

    if data is None:
        return None

    return SessionModel(**data)


def valid_merchant_id(merchant_id: str) -> str:
    data = get_merchant_by_id(merchant_id)

    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "message": "Merchant Id Not Found",
                "errors": [
                    "No Merchant with specified Merchant Id."
                ]
            }
        )

    return data.merchant_id


def valid_session_id(session_id: str) -> str:
    data = get_session_by_id(session_id)

    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "message": "Session Id Not Found",
                "errors": [
                    "No Session with specified Session Id."
                ]
            }
        )

    return data.session_id


def create_studio_session(session_data: SessionCreateModel, merchant_id: str) -> dict():
    session_data.merchant_id = valid_merchant_id(merchant_id)
    session_data.type = session_data.type.value
    create_query = session.insert().values(session_data.dict())
    data = db.fetch_one(create_query.query)
    result = SessionModel(**data)

    return {
        "sessionId": result.session_id
    }


def fetch_studio_sessions(merchant_id: str) -> dict():
    valid_id = valid_merchant_id(merchant_id)
    fetch_query = session.select().where("merchant_id", "=", valid_id)
    data = db.fetch_all(fetch_query.query)
    result = [SessionModel(**item) for item in data]

    return result


def book_session(booking_data: BookingsCreateModel):
    booking_data.session_id = valid_session_id(booking_data.session_id)
    strategy = DerivedStrategy(booking_data)
    ref = BookingRef(strategy)
    booking_data.booking_ref = ref.get_booking_ref()
    create_query = booking.insert().values(booking_data.dict())
    data = db.fetch_one(create_query.query)
    result = BookingsModel(**data)

    return {
        "bookingId": result.booking_id,
        "bookingRef": result.booking_ref
    }


def fetch_bookings(request: Request, limit: int, offset: int, type: AccessType, city: str, merchant: str, period: str):

    fetch_query = booking.select().join("studio_sessions", "studio_sessions.session_id = bookings.session_id").join(
        "merchants", "merchants.merchant_id = studio_sessions.merchant_id").where("merchants.city_of_operation", "LIKE", f"%{city}").and_where(
            "merchants.merchant_id", "LIKE", f"%{merchant}%").paginate(limit, offset)

    data = db.fetch_all(fetch_query)
    result = ResponseCollection(
        count=len(data),
        next=f"{request.base_url}/booking?type={type}&limit={limit}&offset={offset + 1}" if len(data) > limit else "",
        previous=f"" if offset == 1 else f"{request.base_url}/bookings?type={type}&limit={limit}&offset={offset - 1}",
        data=data
    )

    return result
