SELECT employees.name AS emp_name, departments.name AS dept_name,
employees.salary
FROM employees
INNER JOIN departments ON departments.id = employees.dept
AND employees.name like 'C%'
AND salary > (SELECT AVG(salary) FROM employees);