DESC EMPLOYEE;

SELECT employee_id, salary FROM EMPLOYEE WHERE employee_id IN 
(SELECT manager_id FROM EMPLOYEE WHERE salary < 8000) 
ORDER BY employee_id ASC;