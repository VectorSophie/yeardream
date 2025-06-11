DESC score;

SELECT * FROM score WHERE korean = 100 or english = 100 or math = 100;

SELECT * FROM score WHERE korean BETWEEN 70 AND 95 AND english BETWEEN 70 AND 95 AND math BETWEEN 70 AND 95;