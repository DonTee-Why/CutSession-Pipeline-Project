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
    name: str
    email: str
    username: str
    phone_number: str = None

    class Config:
        fields = {
            "user_id": "userId",
            "merchant_id": "merchantId",
            "starts_at": "startsAt",
            "ends_at": "endsAt",
            "session_id": "sessionId",
            "booking_id": "bookingId",
            "booking_ref": "bookingRef",
            "phone_number": "phoneNumber",
            "city_of_residence": "cityOfResidence",
            "city_of_operation": "cityOfOperation",
        }
        allow_population_by_field_name = True

    _required_fields = validator("name", "email", "username", allow_reuse=True, check_fields=False)(utils.required)


class UserBaseModel(BaseClassModel):
    '''
    User Base class. It specifies common attributes for creating and retreiving user data

        Parameters:
            name (string): Name of the user
            email (string): Email address of the user
            phone_number (string): Phone number of the user
    '''
    user_id: str | None
    dob: str
    city_of_residence: str

    _required_fields = validator("dob", "city_of_residence", allow_reuse=True, check_fields=False)(utils.required)


class MerchantBaseModel(BaseClassModel):
    '''
    Merchant Base class. It specifies common attributes for creating and retreiving merchant data

        Parameters:
            city_of_operation (string): Merchant's city of operation
    '''
    merchant_id: str | None
    city_of_operation: str

    _required_fields = validator("city_of_operation", allow_reuse=True, check_fields=False)(utils.required)


class ResponseCollection(BaseModel):
    '''
    Response Collection Class for retreiving a collection of data
    '''
    count: int
    next: str
    previous: str
    data: list = []