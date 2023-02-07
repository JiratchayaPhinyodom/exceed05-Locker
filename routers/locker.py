from fastapi import APIRouter
from . import database

router = APIRouter(
        prefix="/locker"
        )

@router.get("/status")
def show_status():
        all_locker = database.collection.find()
        ret = []
        for d in all_locker:
            del d["_id"]
            ret.append(d)
        return {"result": ret}
        
        

