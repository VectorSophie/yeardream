import pymongo
from pprint import pprint

connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection.get_database("library")
col = db.get_collection("books")

query = {
    "date_received":{
        "$gte":"2014-01-01", 
        "$lte":"2017-12-31"
    }
}
projection = {"_id":True,"title":True}
cursor = col.find(query,projection)

for book in cursor:
    pprint(book)