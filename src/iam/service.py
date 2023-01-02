from datetime import datetime, timedelta
from functools import lru_cache
from fastapi import HTTPException, status, Security, Depends
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    SecurityScopes,
)
from passlib.context import CryptContext
from jose import jwt, JWTError
from pydantic import BaseModel, ValidationError
import uuid
from ..config import AppSettings
from .base_schemas import AccessType, ResponseCollection
from .schemas.auth import AuthModel, AuthResponse
from .schemas.user import UserCreateModel, UserModel, UserInModel
from .schemas.merchant import MerchantCreateModel, MerchantModel, MerchantInModel
from ..database.database import db, User, Merchant


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
user = User()
merchant = Merchant()
settings = AppSettings()

def register_user(user_data: UserCreateModel) -> dict():
    register_query = user.insert().values(user_data.dict())
    data = db.fetch_one(register_query.query)
    result = UserModel(**data)

    return {
        "userId": result.user_id
    }


def register_merchant(merchant_data: MerchantCreateModel) -> dict():
    register_query = merchant.insert().values(merchant_data.dict())
    data = db.fetch_one(register_query.query)
    result = MerchantModel(**data)

    return {
        "merchantId": result.merchant_id
    }


def get_user_by_id(id: str) -> UserModel:
    user_query = user.select().where("user_id", "=", id)
    data = db.fetch_all(user_query.query)
    return UserModel(**data[0])


def get_merchant_by_id(id: str) -> MerchantModel:
    merchant_query = merchant.select().where("merchant_id", "=", id)
    data = db.fetch_all(merchant_query.query)
    return MerchantModel(**data[0])


def get_user(username: str) -> UserInModel:
    user_query = user.select().where("username", "=", username)
    data = db.fetch_all(user_query.query)
    return UserInModel(**data[0])


def get_merchant(username: str) -> MerchantInModel:
    merchant_query = merchant.select().where("username", "=", username)
    data = db.fetch_all(merchant_query.query)
    return MerchantInModel(**data[0])


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(data: AuthModel):
    user = get_user(data.username) if data.access_type.value == "USER" else get_merchant(data.username)

    if not user:
        return False
    if not verify_password(data.password, user.password):
        return False

    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.APP_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


async def authorize(data: AuthModel):
    user = authenticate_user(data)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "message": "Unauthorised",
                "errors": [
                    "Incorrect username or password"
                ]
            }
        )

    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={
            "sub": f"{data.access_type.value}:{user.user_id if data.access_type.value == 'USER' else user.merchant_id}",
            "scopes": [data.access_type.value]
        },
        expires_delta=access_token_expires
    )
    data = {
        "token": access_token,
        "user_id": user.user_id if data.access_type == "USER" else None, 
        "merchant_id": user.merchant_id if data.access_type == "MERCHANT" else None
    }
    auth_res = AuthResponse(**data)

    return auth_res


async def fetch_clients(limit: int, offset: int, type: AccessType, city: str, name: str):
    if type.value == "USER":
        fetch_query = user.select().where("city_of_residence", "LIKE", f"%{city}%").and_where("name", "LIKE", f"%{name}%").paginate(limit, offset)
        user_list = db.fetch_all(fetch_query.query)
        data = [UserModel(**client) for client in user_list]
    elif type.value == "MERCHANT":
        fetch_query = merchant.select().where("city_of_operation", "LIKE", f"%{city}%").and_where("name", "LIKE", f"%{name}%").paginate(limit, offset)
        merchant_list = db.fetch_all(fetch_query.query)
        data=[MerchantModel(**client) for client in merchant_list]
    
    res = ResponseCollection(
        count=len(data),
        next=f"",
        previous=f"",
        data=data
    )

    return res
