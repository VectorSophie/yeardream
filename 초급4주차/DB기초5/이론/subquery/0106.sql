SELECT * FROM emp WHERE birthdate IN 
(SELECT min(birthdate) FROM emp GROUP BY deptno);