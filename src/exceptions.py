from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import request_validation_exception_handler
from starlette.exceptions import HTTPException as StarletteHTTPException


async def http_request_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code, 
        content=jsonable_encoder({
            "message": exc.detail["message"],
            "errors": exc.detail["errors"]
        })
    )

async def request_validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
        content=jsonable_encoder({
            "message": "Unprocessable Entity",
            "errors": [(f"{error['loc'][1]}: {error['msg']}") for error in exc.errors()]
        })
    )

async def server_error_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
        content=jsonable_encoder({
            "message": "Internal Server Error",
            "errors": [(f"{error['loc'][1]} {error['msg']}") for error in exc.errors()]
        })
    )

