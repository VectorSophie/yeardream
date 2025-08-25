import pymongo

connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection.get_database("library")
col = db.get_collection("books")

query={"date_received":{"$regex":"^2015"}}

delete_book = col.delete_many(query)

print(delete_book.deleted_count)