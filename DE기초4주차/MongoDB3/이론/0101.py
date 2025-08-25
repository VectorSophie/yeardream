import pymongo
from pprint import pprint

connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection.get_database("profile")
col = db.get_collection("people")

query = {"name.last": "Cate"}

result = col.update_many(query,{"$unset":{"skills": False}})

cursor = col.find(query)

for people in cursor:
    pprint(people)
