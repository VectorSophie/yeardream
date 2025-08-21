import pymongo
from pprint import pprint

connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection.get_database("library")
col = db.get_collection("books")

data={"title":"Romeo and Juliet", "author": "William Shakespeare", "date_received": "2012-04-01"}
result=col.insert_one(data)
pprint(result.inserted_id)
