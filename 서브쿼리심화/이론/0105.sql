DESC STORE;
DESC PAYMENT;

SELECT store_id, store_name FROM STORE AS s WHERE EXISTS
(SELECT '1000' FROM PAYMENT AS p WHERE p.pay_amount >= 5000 AND p.store_id = s.store_id)
ORDER BY store_id ASC;