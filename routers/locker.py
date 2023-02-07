from fastapi import APIRouter
from database import collection


router = APIRouter(
        prefix="/locker"
        )

@router.get("/status")
def show_status():
        

