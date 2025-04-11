SELECT * FROM emp WHERE sal > 
(SELECT max(sal) FROM emp WHERE job = 'manager')