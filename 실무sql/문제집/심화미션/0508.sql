DESC ELICE_MART;
DESC PRODUCT;

SELECT product_id, product_name FROM ELICE_MART WHERE stock = 0 ORDER BY product_id ASC;

SELECT product_id, product_name FROM ELICE_MART WHERE stock = 0 AND (product_id, product_name) IN (SELECT product_id, product_name FROM PRODUCT WHERE stock >0) ORDER BY product_id ASC;
