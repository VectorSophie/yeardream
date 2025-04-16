DESC EMPLOYEE;

SELECT a.employee_id, a.employee_name, b.employee_name AS manager_name FROM EMPLOYEE AS a, EMPLOYEE AS b WHERE a.manager_id = b.employee_id ORDER BY employee_id ASC;
