from pydantic import root_validator, validator
import uuid

from ..base_schemas import BookingsBaseModel
from ... import utils


class BookingsCreateModel(BookingsBaseModel):
    '''
    Merchant class for creating merchant data

        Parameters:
            booking_id (string): Id of the booking
            booking_ref (string): Ref no of the booking
    '''
    booking_id: str = str(uuid.uuid4())
    booking_ref: str

    # _required_fields = validator("booking_ref", allow_reuse=True)(required)


class BookingsModel(BookingsBaseModel):
    '''
    Booking class for retreiving merchant data

        Parameters:
            booking_id (string): Id of the booking
            booking_ref (string): Ref no of the booking
    '''
    booking_id: str
    booking_ref: str
