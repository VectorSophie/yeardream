DESC EMPLOYEE;

CREATE VIEW EMPLOYEE_DEV AS 
(SELECT employee_id, salary FROM EMPLOYEE WHERE department_name = '개발');

SELECT * FROM EMPLOYEE_DEV;