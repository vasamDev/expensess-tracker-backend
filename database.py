from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["expensesTracker"]
users_collections =db["users"]
expenses_collections = db["expenses"]
