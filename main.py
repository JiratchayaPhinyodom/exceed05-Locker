from pymongo import MongoClient
from dotenv import load_dotenv
import os
import urllib
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Locker

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv(".env")

user = os.getenv("username")
password = urllib.parse.quote(os.getenv("password"))
client = MongoClient(f"mongodb://{user}:{urllib.parse.quote(password)}@mongo.exceed19.online:8443/?authMechanism=DEFAULT")

db = client["exceed05"] #use database name
collection = db['Locker'] #db.collection_name