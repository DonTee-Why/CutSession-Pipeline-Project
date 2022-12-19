from pydantic import BaseModel, EmailStr, root_validator, validator, validate_email
import uuid

from ..base_schemas import SessionBaseModel
from ..utils import required


class SessionCreateModel(SessionBaseModel):
    '''
    Merchant class for creating merchant data

        Parameters:
            id (string): Id of the merchant
    '''
    session_id : str = str(uuid.uuid4())

    _required_fields = validator("session_id", allow_reuse=True)(required)


class SessionModel(SessionBaseModel):
    '''
    Merchant class for retreiving merchant data

        Parameters:
            user_id (string | UUID): ID of the merchant
    '''
    merchant_id: str
