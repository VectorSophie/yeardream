DESC chicken_store;
DESC pizza_store;

SELECT store_name FROM chicken_store WHERE available = 'Y';

SELECT store_name FROM pizza_store WHERE available = 'Y';

SELECT store_name FROM chicken_store WHERE available = 'Y' UNION SELECT store_name FROM pizza_store WHERE available = 'Y' ORDER BY store_name ASC;