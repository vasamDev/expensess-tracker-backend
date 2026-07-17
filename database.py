# from pymongo import MongoClient

# client = MongoClient("mongodb://localhost:27017")
# db = client["expensesTracker"]
# users_collections =db["users"]
# expenses_collections = db["expenses"]



from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

db = client["expensesTracker"]

users_collections = db["users"]
expenses_collections = db["expenses"]