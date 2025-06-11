import csv
import json
from elice_utils import EliceUtils

elice_utils = EliceUtils()

def books_to_json(src_file, dst_file):
    books = []
    with open(src_file) as src:
        reader = csv.reader(src, delimiter=',')
        
        for row in reader:
            book = {
                "title": row[0],
                "author": row[1],
                "genre": row[2],
                "pages": int(row[3]),
                "publisher": row[4]
            }
            books.append(book)
    
    with open(dst_file, 'w') as dst:
        json_string = json.dumps(books)
        dst.write(json_string)

src_file = 'books.csv'
dst_file = 'books.json'
books_to_json(src_file, dst_file)
elice_utils.send_file(dst_file)