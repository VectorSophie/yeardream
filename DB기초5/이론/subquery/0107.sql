SELECT * FROM salaries WHERE salary < all 
(SELECT salary FROM salaries WHERE from_date < '2000-12-31');
SELECT * FROM salaries WHERE salary < any 
(SELECT salary FROM salaries WHERE from_date < '2000-12-31');