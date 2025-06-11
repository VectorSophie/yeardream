DESC BOOK;
DESC BOOK_STOCK;

SELECT book_id, book_name, book_writer, price FROM BOOK WHERE 
(book_name, book_writer) IN 
(SELECT book_name, book_writer FROM BOOK_STOCK WHERE stock >= 1)
ORDER BY book_id ASC;