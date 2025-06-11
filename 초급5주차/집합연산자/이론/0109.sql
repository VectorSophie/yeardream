DESC book_store_a;
DESC book_store_b;

SELECT book_name FROM book_store_a WHERE stock > 0;

SELECT book_name FROM book_store_b WHERE stock > 0;

SELECT book_name FROM book_store_a WHERE stock > 0 EXCEPT SELECT book_name FROM book_store_b WHERE stock > 0;