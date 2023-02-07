from pymongo import MongoClient
from dotenv import load_dotenv
import os
import urllib
from fastapi import FastAPI

load_dotenv(".env")

user = os.getenv("username")
password = urllib.parse.quote(os.getenv("password"))
client = MongoClient(f"mongodb://{user}:{urllib.parse.quote(password)}@mongo.exceed19.online:8443/?authMechanism=DEFAULT")

db = client["exceed05"] #use database name
collection = db['Locker'] #db.collection_name


app = FastAPI()


@app.get("/")
def root():
    return "Hi"
