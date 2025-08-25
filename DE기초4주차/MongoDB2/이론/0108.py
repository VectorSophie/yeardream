import pymongo

connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection.get_database("library")
col = db.get_collection("books")

update={"$set":{"author":"Joanne Kathleen Rowling"}}
query={"title":{"$regex":"Harry Potter"}}

update_book = col.update_many(query,update)

print(update_book.modified_count)

for x in col.find():
    print(x)
