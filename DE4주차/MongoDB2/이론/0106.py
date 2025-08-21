import pymongo
from pprint import pprint

connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection.get_database("library")
col = db.get_collection("books")

projection={"_id": False}
cursor=col.find({},projection)
for doc in cursor:
    pprint(doc)
