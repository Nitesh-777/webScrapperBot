import json
from pymongo import MongoClient

with open('config.json') as f:
    config = json.load(f)

client = MongoClient(config['mongo_uri'])
db = client[config['database_name']]

# testing database
test_collection = db['products']
test_collection.insert_one({"name": "toothbrush", "price": 3})
test_collection.insert_one({"name": "pencil", "price": 0.50})
test_collection.insert_one({"name": "glue", "price": 2})

# print all collections in the 'webscrapperData' database
print(db.list_collection_names())