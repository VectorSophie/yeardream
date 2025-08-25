import pymongo

connection = pymongo.MongoClient("mongodb://localhost:27017/")

db = connection.get_database("library")

col = db.get_collection("books")
data = col.insert_one({ "title": "Harry Potter and the Deathly Hallows", "author": "Joanne Kathleen Rowling","publisher": "Bloomsbury Publishing" ,"date_received": "2017-07-21"})


result = connection.list_database_names()

print(result)