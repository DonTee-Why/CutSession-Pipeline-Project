from fastapi import APIRouter
from fastapi import Depends
from ..installation import service

router = APIRouter()

@router.get("/db/install")
def install_tables():
    return service.install_tables()