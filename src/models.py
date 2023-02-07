from fastapi import FastAPI, Body
from typing import Union, Optional
from pydantic import BaseModel

class Item(BaseModel):
    item_id : Union[int, str]
    item_name: str = "   "
    item_bool: bool

class ItemDetail(BaseModel):
    item_color: str
    item_detail: str