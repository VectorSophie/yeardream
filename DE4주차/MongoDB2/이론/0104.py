import pymongo
from pprint import pprint

connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection.get_database("library")
col = db.get_collection("books")

new_book1 = {"title": "Alice\'s Adventures in Wonderland", "author": "Lewis Carroll", "publisher": "Macmillan", "date_received": "2015-11-26"}
new_book2 = {"title": "The Old Man and the Sea", "author": "Ernest Miller Hemingway","publisher": "Charles Scribner\'s Sons" ,"date_received": "2014-11-02"}
new_book3 = {"title": "The Great Gatsby", "author": "Francis Scott Key Fitzgerald", "date_received": "2019-01-12"}

data=[new_book1,new_book2,new_book3]
result=col.insert_many(data)

pprint(result.inserted_ids)
