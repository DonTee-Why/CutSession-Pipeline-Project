from typing import Any

from .schemas.user import UserCreateModel, UserModel
from .schemas.merchant import MerchantCreateModel, MerchantModel
from ..database.database import db, user, merchant


def register_user(user_data: UserCreateModel) -> Any:
    register_query = user.insert().values(user_data.dict())
    data = db.fetch_one(register_query.query)
    result = UserModel().from_list(data)

    return {
        "userId": result.user_id
    }

def register_merchant(merchant_data: MerchantCreateModel) -> Any:
    register_query = merchant.insert().values(merchant_data.dict())
    data = db.fetch_one(register_query.query)
    result = MerchantModel().from_list(data)

    return {
        "merchantId": result.merchant_id
    }
