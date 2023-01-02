from pydantic import validator, Field
from ..base_schemas import UserBaseModel
from ... import utils



class UserCreateModel(UserBaseModel):
    '''
    User class for creating user data.

        Parameters:
            name (string): Name of the user
            email (string): Email address of the user
            username (string): Username of the user
            phoneNumber (string): Phone number of the user
            dob (date): Date of birth of the user
            cityOfResidence (string): City of Residence of the user
            password (string): Password of the user
    '''
    user_id: str = None
    username: str
    password: str
    email: str

    _generate_id = validator("user_id", pre=True, always=True, allow_reuse=True)(utils.generate_uuid)
    _required_fields = validator("username","password", allow_reuse=True)(utils.required)
    _valid_email = validator("email", allow_reuse=True)(utils.email)
    _valid_name = validator("name", allow_reuse=True)(utils.name)
    _valid_name = validator("dob", allow_reuse=True)(utils.valid_date)
    _valid_min_length = validator("password", "username", allow_reuse=True)(utils.valid_min_length)
    _valid_max_length = validator("city_of_residence", "username", "phone_number", allow_reuse=True)(utils.valid_max_length)
    _valid_length_range = validator("city_of_residence", "phone_number", allow_reuse=True)(utils.valid_length_range)
    _hash_password = validator("password", allow_reuse=True)(utils.hash_password)


class UserModel(UserBaseModel):
    '''
    User class for reading user data

        Parameters:
            user_id (string): ID of the user
            name (string): Name of the user
            email (string<email>): Email address of the user
            username (string): Username of the user
            phoneNumber (string): Phone number of the user
            dob (date): Date of birth of the user
            cityOfResidence (string): City of Residence of the user
    '''
    user_id: str


class UserInModel(UserBaseModel):
    '''
    Merchant class for retreiving merchant data

        Parameters:
            password (string): merchant password
    '''
    password: str
