from pydantic import validator, Field
from ..base_schemas import MerchantBaseModel
from ..utils import required, email as valid_email, valid_length_range, valid_max_length, valid_min_length, name, valid_date, generate_uuid


class MerchantCreateModel(MerchantBaseModel):
    '''
    Merchant class for creating merchant data

        Parameters:
            name (string): Name of the user
            email (string): Email address of the user
            phone_number (string): Phone number of the user
            password (string): Password of the merchant
            city_of_operation (string): Merchant's city of operation
    '''

    username: str
    password: str
    email: str
    merchant_id: str | None

    _required_fields = validator("password", "username", allow_reuse=True)(required)
    _generate_id = validator("merchant_id", allow_reuse=True, check_fields=False)(generate_uuid)
    _valid_email = validator("email", allow_reuse=True)(valid_email)
    _valid_name = validator("name", allow_reuse=True)(name)
    _valid_min_length = validator("password", "username", allow_reuse=True)(valid_min_length)
    _valid_max_length = validator("username", "phone_number", allow_reuse=True)(valid_max_length)
    _valid_length_range = validator("city_of_operation", "phone_number", allow_reuse=True)(valid_length_range)


class MerchantModel(MerchantBaseModel):
    '''
    Merchant class for retreiving merchant data

        Parameters:
            user_id (string | UUID): ID of the merchant
    '''
    merchant_id: str
