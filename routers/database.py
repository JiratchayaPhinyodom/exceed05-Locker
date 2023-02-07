from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv(".env")

USER = os.getenv("username")
PASSWORD = os.getenv("password")
client = MongoClient(f"mongodb://{USER}:{PASSWORD}@mongo.exceed19.online:8443/?authMechanism=DEFAULT")

db = client["exceed05"] #use database name
collection = db['Locker'] #db.collection_name
