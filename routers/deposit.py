from fastapi import APIRouter
from .database import collection
from datetime import datetime



router = APIRouter(
        prefix="/deposit",
        )

@router.get("/user/{user_id}/{time_deposit}/{user_item}")
def insert_user(user_id: int, time_deposit: int, user_item: str):
    print(list(collection.find({'Locker': {'locker_id': 1}})))
#     collection.insert_one({"user_id":user_id, "time_deposit":time_deposit, "user_item":user_item})
    return {"user_id":user_id, "time_deposit":time_deposit, "user_item":user_item}

