SELECT * FROM emp WHERE birthdate > 
(SELECT birthdate FROM emp WHERE empnum = 7) ;