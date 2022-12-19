from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
import uvicorn

from .routers import db, iam
from .exceptions import request_validation_exception_handler, http_exception_handler

app = FastAPI()

app.include_router(db.router)
app.include_router(iam.register_router)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return await request_validation_exception_handler(request, exc)

# @app.exception_handler(StarletteHTTPException)
# async def http_exception_handler(request, exc):
#     return await http_exception_handler(request, exc)


@app.get("/")
def hello():
    return {"data": "Hello there!"}

if __name__ == "__main__":
    uvicorn.run(app)