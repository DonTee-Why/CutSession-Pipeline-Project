from datetime import datetime
from pydantic import validate_email
from passlib.context import CryptContext
# from .config import settings
import uuid


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def generate_uuid(value: str) -> str:
    value = str(uuid.uuid4())
    return value


def required(value: str):
    if value is None:
        raise ValueError(f"Field is required")
    return value


def name(value):
    if not len(value) >= 2 and not len(value) <= 25:
        raise ValueError(f"Field should have between 2 to 25 characters")
    return value


def valid_max_length(value):
    if not len(value) <= 20:
        raise ValueError(f"Field exceeds limit of 20 characters")
    return value


def valid_min_length(value):
    if not len(value) >= 6:
        raise ValueError(f"Field should have at least 6 characters")
    return value


def valid_length_range(value):
    if not len(value) >= 6 and not len(value) <= 20:
        raise ValueError(f"Field exceeds limit of 20 characters")
    return value


def valid_date(value):
    try:
        datetime.strptime(value, '%Y-%m-%d')
    except Exception:
        raise ValueError("Incorrect date format. Date format should be YYYY-MM-DD")
    return value


def email(value):
    if len(value) > 50:
        raise ValueError(f"Field exceeds limit of 50 characters")
    valid_email = validate_email(value)
    return valid_email[1]


def hash_password(password: str):
    return pwd_context.hash(password)

