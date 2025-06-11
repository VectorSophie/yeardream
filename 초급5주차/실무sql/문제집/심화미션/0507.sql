DESC STORE;

SELECT sales_amount FROM STORE WHERE store_location = '남부' ORDER BY sales_amount ASC;

SELECT store_id, store_name, store_location, sales_amount FROM STORE WHERE sales_amount > ALL(SELECT sales_amount FROM STORE WHERE store_location = '남부') ORDER BY store_id ASC;