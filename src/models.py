from fastapi import FastAPI, Body
from typing import Union, Optional
from pydantic import BaseModel

class User(BaseModel):
    user_id : int
    time_deposit: int
    user_item: str
    pay: int

class Locker(BaseModel):
    locker_id: int
    is_avaliable: bool