import csv

def print_book_info(filename):
    with open(filename) as file:
        reader = csv.reader(file, delimiter=',')
        
        for row in reader:
            
            title = row[0]
            author = row[1]
            pages = row[3]
            print("{} ({}): {}p".format(title, author, pages))

filename = 'books.csv'
print_book_info(filename)