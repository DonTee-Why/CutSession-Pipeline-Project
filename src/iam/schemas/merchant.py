from pydantic import BaseModel, EmailStr, root_validator, validator, validate_email
import uuid
from ..base_schemas import BaseClassModel, MerchantBaseModel
from ..utils import required


class MerchantCreateModel(MerchantBaseModel):
    '''
    Merchant class for creating merchant data

        Parameters:
            password (string): Password of the merchant
    '''
    username: str
    password: str

    _required_fields = validator("password", "username", allow_reuse=True)(required)


class MerchantModel(MerchantBaseModel):
    '''
    Merchant class for retreiving merchant data

        Parameters:
            user_id (string | UUID): ID of the merchant
    '''
    merchant_id: str
