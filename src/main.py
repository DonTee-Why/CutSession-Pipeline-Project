from typing import Union
from fastapi import FastAPI, Depends, HTTPException
import uvicorn

from .routers import db

app = FastAPI()

app.include_router(db.router)

@app.get("/")
def hello():
    return {"data": "Hello there!"}

if __name__ == '__main__':
    uvicorn.run(app)