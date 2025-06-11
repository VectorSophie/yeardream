SELECT AVG(sal) FROM emp WHERE deptno = 40;

SELECT *, 
FLOOR( (CAST(REPLACE(CURRENT_DATE,'-','') AS UNSIGNED) - CAST(REPLACE(birthdate,'-','') AS UNSIGNED)) / 10000 ) 
AS age FROM emp WHERE sal >
(SELECT AVG(sal)FROM emp WHERE deptno = 40) ;