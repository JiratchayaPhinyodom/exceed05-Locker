from fastapi import FastAPI, Body
from typing import Union, Optional
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
class Locker(BaseModel):
    locker_id: int
    is_avaliable: bool
    time_deposit: Optional[int]
    user_item: Optional[list[str]]
    start_time: Optional[int]
