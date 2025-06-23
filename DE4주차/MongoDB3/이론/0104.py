import pymongo
from pprint import pprint

connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection.get_database("library")
col = db.get_collection("books")

query1 = {
    "date_received": {
        "$gte": "2014-01-01",
        "$lt": "2015-01-01"
    }
}
query2 = {
    "date_received": {
        "$gte": "2019-01-01",
        "$lt": "2020-01-01"
    }
}

query = {
    "$or": [query1, query2]
}
cursor = col.find(query)

for book in cursor:
    pprint(book)