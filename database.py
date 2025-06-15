from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["expense_tracker_db"]
expenses_collection = db["expenses"]
budgets_collection = db["budgets"]
