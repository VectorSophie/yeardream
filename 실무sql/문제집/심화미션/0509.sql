DESC EMPLOYEE;
DESC DEPARTMENT;

CREATE VIEW EMPLOYEE_DEPARTMENT AS 
(SELECT employee_id,employee_name,salary, E.department_id, department_name FROM EMPLOYEE E INNER JOIN DEPARTMENT D ON E.department_id = D.department_id);
SELECT * FROM EMPLOYEE_DEPARTMENT;