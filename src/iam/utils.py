from fastapi.exceptions import RequestValidationError
from pydantic import validator, validate_email, ValidationError
import uuid


def generate_uuid(value: str) -> str:
    return str(uuid.uuid4())

def required(value: str):
    if value is None:
        raise ValueError(f"field is required!!!")
    return value

def name(value):
    if not len(value) >= 2 and not len(value) <= 25:
        raise ValueError(f"field should have between 2 to 25 characters")
    return value

def valid_max_length(value):
    if not len(value) <= 20:
        raise ValueError(f"field exceeds limit of 20 characters")
    return value

def valid_min_length(value):
    if not len(value) >= 6:
        raise ValueError(f"field should have at least 6 characters")
    return value

def valid_length_range(value):
    if not len(value) >= 6 and not len(value) <= 20:
        raise ValueError(f"field exceeds limit of 20 characters")
    return value

def email(value):
    if len(value) > 50:
        raise ValueError(f"field exceeds limit of 50 characters")
    valid_email = validate_email(value)
    return valid_email[1]


class CustomValidators(object):
    def required(value: str = None):
        if value is None:
            value = value.replace("_", " ")
            raise ValueError(f"field is required")
        return value

    def email(v):
        valid_email = validate_email(v)
        return valid_email[1]


if __name__ == "__main__":
    validators = CustomValidators()
