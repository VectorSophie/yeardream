SELECT DISTINCT emp_no, 
(SELECT avg(salary) FROM salaries AS A WHERE A.emp_no = B.emp_no) 
AS avg_salary FROM salaries AS B;