DESC FOOD;

SELECT food_id, food_type, food_name, price FROM FOOD WHERE price >ANY
(SELECT price FROM FOOD WHERE food_type = 'Main') 
ORDER BY food_id ASC;