UPDATE product SET stock = 0 WHERE id = 1;
UPDATE product SET stock = 50 WHERE id = 3;
UPDATE product SET selling_price = 800 WHERE id = 2;
DELETE FROM product WHERE id = 4;

SELECT * FROM product;