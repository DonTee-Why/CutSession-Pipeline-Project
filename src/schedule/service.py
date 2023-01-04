from datetime import datetime, timedelta
from fastapi import HTTPException, status, Security, Depends
from ..config import AppSettings
# from .base_schemas import AccessType, ResponseCollection
from ..iam.schemas.user import UserCreateModel, UserModel, UserInModel
from ..iam.schemas.merchant import MerchantModel, MerchantInModel
from .schemas.session import SessionCreateModel, SessionModel
from ..database.database import db, User, Merchant, Session, Booking


user = User()
merchant = Merchant()
session = Session()
booking = Booking()
settings = AppSettings()


def get_merchant_by_id(id: str) -> MerchantModel:
    merchant_query = merchant.select().where("merchant_id", "=", id)
    data = db.fetch_one(merchant_query.query)

    if data is None:
        return None

    return MerchantModel(**data)


def valid_merchant_id(merchant_id: str) -> str:
    data = get_merchant_by_id(merchant_id)

    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "message": "Merchant Id Not Found",
                "errors": [
                    "No Merchant with specified Merchant Id."
                ]
            }
        )
    
    return data.merchant_id


def create_studio_session(session_data: SessionCreateModel, merchant_id: str) -> dict():
    valid_id = valid_merchant_id(merchant_id)
    session_data.merchant_id = valid_id
    session_data.type = session_data.type.value
    sess_dict = session_data.dict()
    create_query = session.insert().values(session_data.dict())
    data = db.fetch_one(create_query.query)
    result = SessionModel(**data)

    return {
        "sessionId": result.session_id
    }


def fetch_studio_sessions(merchant_id: str) -> dict():
    fetch_query = session.select().where("merchant_id", "=", merchant_id)
    data = db.fetch_all(fetch_query.query)
    result = [SessionModel(**item) for item in data]

    return result
