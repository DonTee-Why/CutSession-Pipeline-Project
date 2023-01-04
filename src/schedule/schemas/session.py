from pydantic import validator
from ..base_schemas import SessionBaseModel
from ... import utils


class SessionCreateModel(SessionBaseModel):
    '''
    Merchant class for creating merchant data

        Parameters:
            id (string): Id of the merchant
    '''
    session_id : str = None

    _generate_id = validator("session_id", pre=True, always=True, allow_reuse=True)(utils.generate_uuid)
    _required_fields = validator("starts_at", "ends_at", "type", allow_reuse=True)(utils.required)
    _valid_date = validator("starts_at", "ends_at", allow_reuse=True)(utils.valid_time)


class SessionModel(SessionBaseModel):
    '''
    Session class for retreiving session data

        Parameters:
            merchant_id (string): ID of the merchant
    '''
    session_id: str
    merchant_id: str
