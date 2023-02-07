from fastapi import APIRouter
from . import database

router = APIRouter(
        prefix="/locker"
        )

@router.get("/status")
def show_status():
        all_locker = database.collection.find()
        ret = []
        for dd in all_locker:
                print(dd)
                d = dd["Locker"]
                ret.append({"locker_id": d["locker_id"], "is_available": d["is_available"]})
        return {"result": ret}
        
        

