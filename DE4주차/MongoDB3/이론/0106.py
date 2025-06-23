import pymongo
from pprint import pprint

connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection.get_database("library")
col = db.get_collection("books")

col.create_index([('title', pymongo.TEXT)], default_language='english')

query = {
    "$text": {
        "$search": "harry"
    }
}
cursor = col.find(query)

for book in cursor:
    pprint(book)
