from fastapi import APIRouter
from ..main import Depends
from ..db import service

router = APIRouter()

@router.get("/db/install")
def install_tables():
    return service.install_tables()