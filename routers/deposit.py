from fastapi import APIRouter
from .database import collection
from datetime import datetime



router = APIRouter(
        prefix="/deposit",
        )

@router.post("/user/{user_id}/{time_deposit}/{user_item}/{locker_id}")
def insert_user(user_id: int, time_deposit: int, user_item: str, locker_id: int):
#     print(collection.find({'Locker': {'locker_id': 1}}))
    collection.update_one({'locker_id': locker_id}, 
                          {"$set":{"user_id":user_id, "time_deposit":time_deposit, 
                                   "user_item":user_item, "timestamp":round(datetime.now().timestamp())}})
    return {"user_id":user_id, "time_deposit":time_deposit, "user_item":user_item, "timestamp":round(datetime.now().timestamp())}

@router.post("/pay/{user_id}/{locker_id}")
def payment(user_id: int, locker_id: int):
        res = collection.find_one({"user_id": user_id ,"locker_id": locker_id}, {"_id":0})
        current_time = round(datetime.now().timestamp())
        time_spent = round((current_time - res["timestamp"])/60)
        if time_spent < 120:  
                collection.update_one({'locker_id': locker_id}, 
                                {"$set":{"pay": 0}})
                return {"Pay": 0}
        else:
               if res["time_deposit"] > time_spent:
                      money = round(((res["time_deposit"] - time_spent)/60)*5)
                      collection.update_one({'locker_id': locker_id}, 
                                {"$set":{"pay": money}})
                      return {"Pay": money}
               else:
                      if res["time_deposit"] > 120:
                             deduct_freetime = time_spent - 120
                             intime = res["time_deposit"] - 120
                             overtime = deduct_freetime - intime
                             money = round((intime/60)*5) + round((overtime/10)*20)
                             collection.update_one({'locker_id': locker_id}, 
                                {"$set":{"pay": money}})
                             return {"Pay": money}
                      else:
                             overtime = time_spent - res["time_deposit"]
                             money = round((overtime/10)*20)                             
                             collection.update_one({'locker_id': locker_id}, 
                                {"$set":{"pay": money}})
                             return {"Pay": money}
                      
                      
                      


