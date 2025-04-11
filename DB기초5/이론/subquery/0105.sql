SELECT * FROM emp WHERE sal = any 
(SELECT max(sal) FROM emp GROUP BY deptno);