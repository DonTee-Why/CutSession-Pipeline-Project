from typing import Any

from .schemas.user import UserCreateModel
from ..database.database import db, user


def register_user(user_data: UserCreateModel) -> Any:
    register_query = user.insert().values(user_data.dict())
    result = db.fetch_one(register_query.query)
    return {
        "userId": result[0]
    }
