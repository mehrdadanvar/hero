import pymongo
import os
from dotenv import load_dotenv
from pymongo import MongoClient

client = MongoClient()
load_dotenv()
secret = os.getenv("MONGO_URI")
client = MongoClient(secret)
print("client connected")
database = client["hhh"]
print("db connected")
