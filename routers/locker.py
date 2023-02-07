from fastapi import APIRouter



router = APIRouter(
        prefix="/locker"
        )


@router.get("/locker/status/{locker_id}")
def locker_status(locker_id: int):
   pass

@router.get("/locker/get_all_locker")
def get
