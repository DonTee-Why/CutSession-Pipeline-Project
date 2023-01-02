from enum import Enum
from pydantic import BaseModel, validator
from fastapi.security import OAuth2PasswordRequestForm
from ... import utils
from ..base_schemas import AccessType


class AuthModel(BaseModel, OAuth2PasswordRequestForm):
    '''
    General Auth Model class. It specifies authentication attributes of users and merchants

        Parameters:
            username (string): Username of the user
            password (string): Password of the user
    '''
    username: str
    password: str
    access_type: AccessType

    class Config:
        fields = {
            "access_type": "accessType",
        }


class AuthResponse(BaseModel):
    '''
    Auth Response Model class. It specifies authentication response attributes of users and merchants

        Parameters:
            username (string): Username of the user
            password (string): Password of the user
    '''
    token: str
    user_id: str | None
    merchant_id: str | None

    class Config:
        fields = {
            "user_id": "userId",
            "merchant_id": "merchantId",
        }
        allow_population_by_field_name = True

    _required_fields = validator("token", allow_reuse=True)(utils.required)
