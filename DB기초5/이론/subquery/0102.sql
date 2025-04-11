SELECT * FROM emp WHERE sal < 
(SELECT AVG(sal) FROM emp);