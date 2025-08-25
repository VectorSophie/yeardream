import pymongo

connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection.get_database("library")
col = db.get_collection("books")

col.update_one({"title": "The Rings of Lord"}, {"$set":{"title":"The Lord of the Rings"}})

for x in col.find():
    print(x)