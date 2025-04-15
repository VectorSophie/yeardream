DESC student;
DESC lecture_special;

SELECT name, email FROM student;

SELECT name, email FROM lecture_special;

SELECT name, email FROM student INTERSECT SELECT name, email FROM lecture_special;