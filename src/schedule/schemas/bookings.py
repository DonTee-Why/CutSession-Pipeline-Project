from pydantic import validator
import uuid

from ..base_schemas import BookingsBaseModel
from ... import utils


class BookingsCreateModel(BookingsBaseModel):
    '''
    Merchant class for creating merchant data

        Parameters:
            booking_id (string): Id of the booking
            booking_ref (string): Booking reference number
    '''
    booking_id: str | None
    booking_ref: str | None

    _generate_id = validator("booking_id", pre=True, always=True, allow_reuse=True)(utils.generate_uuid)
    _required_fields = validator("user_id", "date", allow_reuse=True)(utils.required)
    _valid_date = validator("date", allow_reuse=True)(utils.valid_date)


class BookingsModel(BookingsBaseModel):
    '''
    Booking class for retreiving merchant data

        Parameters:
            booking_id (string): Id of the booking
            booking_ref (string): Ref no of the booking
    '''
    booking_id: str
    booking_ref: str
