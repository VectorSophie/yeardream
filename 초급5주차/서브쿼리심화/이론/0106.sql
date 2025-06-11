DESC EMPLOYEE;

SELECT salary FROM EMPLOYEE WHERE position = '사원' ORDER BY salary ASC;

SELECT employee_id, salary, position FROM EMPLOYEE WHERE salary >= ALL
(SELECT salary FROM EMPLOYEE WHERE position = '사원') 
ORDER BY employee_id ASC;
