from typing import Optional
from datetime import datetime, date
from enum import Enum
from pydantic import BaseModel, validator
from .. import utils


class SessionType(str, Enum):
    WEEKDAY = "WeekDay"
    WEEKEND = "WeekEnd"


class AccessType(str, Enum):
    USER = "USER"
    MERCHANT = "MERCHANT"


class BaseClassModel(BaseModel):
    '''
    General Base class. It specifies common attributes of users and merchants

        Parameters:
            name (string): Name of the user
            email (string): Email address of the user
            phone_number (string): PPhone number of the user
    '''
    session_id: str | None

    class Config:
        fields = {
            "user_id": "userId",
            "merchant_id": "merchantId",
            "starts_at": "startsAt",
            "ends_at": "endsAt",
            "session_id": "sessionId",
            "booking_id": "bookingId",
            "booking_ref": "bookingRef",
        }
        allow_population_by_field_name = True
        use_enum_values = True

    _required_fields = validator("name", "email", "username", allow_reuse=True, check_fields=False)(utils.required)


class SessionBaseModel(BaseClassModel):
    '''
    General Base class. It specifies common attributes for creating and retreiving studio sessions

        Parameters:
            merchant_id (string): Id of the merchant
            starts_at (string): The time the session starts
            ends_at (string): The time the session ends
            type (string): Type of session (either weekday or weekend sessions)
    '''
    merchant_id: str | None
    starts_at: str
    ends_at: str
    type: SessionType

    _required_fields = validator("*", allow_reuse=True, check_fields=False)(utils.required)

class BookingsBaseModel(BaseClassModel):
    '''
    General Base class. It specifies common attributes for creating and retreiving studio sessions

        Parameters:
            session_id (string): Id of the session
            user_id (string): Id of the user
            booking_ref (string): Booking reference number
            date (date): Date
            notes (string): Additional notes
            title (string): Session title
    '''
    user_id: str | None
    booking_ref: str | None
    date: str | None
    notes: str | None
    title: str | None

    _required_fields = validator("session_id", "user_id", "date", "starts_at", "ends_at", allow_reuse=True, check_fields=False)(utils.required)

class ResponseCollection(BaseModel):
    '''
    Response Collection Class for retreiving a collection of data

        Parameters:
            merchant_id (string): Id of the merchant
            starts_at (string): The time the session starts
            ends_at (string): The time the session ends
            type (string): Type of session (either weekday or weekend sessions)
            notes (string): Additional notes
            title (string): Session titles
    '''
    count: int
    next: str
    previous: str
    data: list = []
