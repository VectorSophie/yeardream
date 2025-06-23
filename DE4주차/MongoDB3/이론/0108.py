import pymongo
from pprint import pprint

connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection.get_database("profile")
col = db.get_collection("people")

query = {"skills.name": {"$all":["Ruby","Python",]}}
cursor = col.find(query)

for people in cursor:
    pprint(people)

query = {"skills": {"$size":4}}
cursor = col.find(query)

for people in cursor:
    pprint(people)
