from fastapi import APIRouter
from .database import collection
from datetime import datetime, timedelta
from src.models import Locker


router = APIRouter(
        prefix="/deposit",
        )

@router.post("/reserve")
def insert_user(locker: Locker):
    lk = collection.find_one({"locker_id": locker.locker_id}, {"_id":False})
    if lk["is_available"] is True:
        collection.update_one({'locker_id': locker.locker_id}, 
                                {"$set":{"user_id":locker.user_id, "time_deposit":locker.time_deposit, 
                                        "user_item":locker.user_item, "timestamp":round(datetime.now().timestamp()), "is_available":False}})
        return {"user_id":locker.user_id, "time_deposit":locker.time_deposit, "user_item":locker.user_item, "timestamp":round(datetime.now().timestamp())}
    else:
         return {"Unable to reserve now"}

@router.get("/get_price")
def get_price(locker: Locker):
#     user_id: int, locker_id: int
    lk = collection.find_one({"user_id": locker.user_id, "locker_id": locker.locker_id}) 
    if not lk:
            return
    start = lk["timestamp"]
    start_dt = datetime.fromtimestamp(start)
    time_deposit_min = lk["time_deposit"]

    time_deposit_dt = start_dt + timedelta(minutes=time_deposit_min)

    diff = time_deposit_dt - start_dt

    current_time = datetime.now()

    fee = 0

    if current_time > time_deposit_dt:
            fee += 20 * ((current_time - time_deposit_dt).total_seconds() / 600) //1

    if diff <= timedelta(hours=2):
            collection.update_one({"locker_id": locker.locker_id}, {"$set": {"price": fee}})
            return fee

    fee += 5 * (diff - timedelta(hours=2)).total_seconds() / 3600
    collection.update_one({"locker_id": locker.locker_id}, {"$set": {"price": fee}})
    return fee

@router.get("/pay/{money}")
def real_pay(locker: Locker, money:int):
        # money: int, locker_id: int
        lk = collection.find_one({"locker_id": locker.locker_id}, {"_id": 0})
        if not locker:
                return "Please try again."

        if money < lk["price"]:
                return "์Not enough money to pay"
        else:
                collection.update_one({"locker_id": locker.locker_id}, {"$set": {"is_available": True}})
                if money - lk["price"] > 0:
                        return money - lk["price"]
                else:
                        return 0

                      
                      
                      


