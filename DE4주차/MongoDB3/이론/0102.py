import pymongo
from pprint import pprint
import re

connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection.get_database("library")
col = db.get_collection("books")

query = {"date_received": 
    {"$nin": [
        re.compile("^2015"), 
        re.compile("^2017")
    ]}
}

col.delete_many(query)