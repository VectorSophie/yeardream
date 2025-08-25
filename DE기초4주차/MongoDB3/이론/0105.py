import pymongo
from pprint import pprint

connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection.get_database("library")
col = db.get_collection("books")

query1 = {"$or": 
    [{"author": "Antoine de Saint-Exupery"},
    {"author": "Ernest Miller Hemingway"}]
}

query2 = {"$or":
    [{"date_received": {"$regex": "^2014"}},
    {"date_received": {"$regex": "^2019"}}]
}

query = {"$and": [query1,query2]}
cursor = col.find(query)

for book in cursor:
    pprint(book)