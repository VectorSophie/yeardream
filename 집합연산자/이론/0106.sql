DESC lecture_basic;
DESC lecture_special;

SELECT student_number,student_name FROM lecture_basic;

SELECT student_number,student_name FROM lecture_special;

SELECT student_number,student_name FROM lecture_basic INTERSECT SELECT student_number,student_name FROM lecture_special;