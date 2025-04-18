DESC STUDENT;

SELECT ID, MATH, PHYSICS, CHEMISTRY,
(MATH+PHYSICS+CHEMISTRY) AS SCORE_NUM,PERCENT_RANK() OVER
(ORDER BY SCORE_NUM DESC) AS PERCENT_RANK, CUME_DIST() OVER 
(ORDER BY SCORE_NUM DESC) AS CUME_DIST FROM STUDENT ORDER BY SCORE_NUM DESC;