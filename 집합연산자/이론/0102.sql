DESC lecture_basic;
DESC lecture_special;

SELECT student_number,student_name FROM lecture_basic;

SELECT student_number,student_name FROM lecture_special;

SELECT student_number,student_name FROM lecture_basic UNION SELECT student_number,student_name FROM lecture_special ORDER BY student_number ASC;