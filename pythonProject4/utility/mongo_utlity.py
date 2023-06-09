from scripts.constants.app_constants import Database
from pymongo import MongoClient


client = MongoClient(Database.db_uri)
db = client[Database.db_name]
collection = db[Database.db_collection]