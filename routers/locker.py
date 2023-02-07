from fastapi import APIRouter
from .database import *

router = APIRouter(
        prefix="/locker"
        )

@router.get("/status")
def show_status():
    pass
        

