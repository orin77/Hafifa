from pymongo import MongoClient

def get_db():
    client = MongoClient("mongo://localhost:27017/")
    db = client['achievement_tracker']
    return db
