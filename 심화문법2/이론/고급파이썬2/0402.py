import csv

def get_titles_of_long_books(books_csv):
    with open(books_csv) as books:
        reader = csv.reader(books, delimiter=',')
        is_long = lambda row: int(row[3])> 250
        get_title = lambda row: row[0]
        
        long_books = filter(is_long, reader)
        long_book_titles = map(get_title, long_books)
        
        return list(long_book_titles)

books  = 'books.csv'
titles = get_titles_of_long_books(books)
for title in titles:
    print(title)
