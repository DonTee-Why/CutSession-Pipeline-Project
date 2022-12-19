from fastapi import FastAPI
import uvicorn

from .routers import db, iam
from .exceptions import request_validation_exception_handler, http_exception_handler

app = FastAPI()

app.include_router(db.router)
app.include_router(iam.register_router)

@app.get("/")
def hello():
    return {"data": "Hello there!"}

if __name__ == "__main__":
    uvicorn.run(app)