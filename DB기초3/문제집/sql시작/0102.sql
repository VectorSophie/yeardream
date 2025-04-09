SELECT *, weight / ((height/100)*(height/100))
FROM student;
SELECT *, weight / ((height/100)*(height/100))
FROM student
WHERE weight / ((height/100)*(height/100)) <= 18.5 OR weight /
((height/100)*(height/100)) >=25.0;