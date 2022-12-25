from typing import Any

from .schemas.user import UserCreateModel
from .schemas.merchant import MerchantCreateModel
from ..database.database import db, user, merchant


def register_user(user_data: UserCreateModel) -> Any:
    register_query = user.insert().values(user_data.dict())
    result = db.fetch_one(register_query.query)

    return {
        "userId": result[0]
    }

def register_merchant(merchant_data: MerchantCreateModel) -> Any:
    register_query = merchant.insert().values(merchant_data.dict())
    result = db.fetch_one(register_query.query)

    return {
        "merchantId": result[0]
    }
