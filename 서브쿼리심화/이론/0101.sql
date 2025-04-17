DESC EMPLOYEE;

SELECT a.employee_id  FROM EMPLOYEE a WHERE a.salary>=
(SELECT salary FROM EMPLOYEE b WHERE a.manager_id = b.employee_id) 
ORDER BY employee_id ASC;