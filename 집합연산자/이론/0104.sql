DESC lecture_basic;
DESC lecture_special;

SELECT lecture_name FROM lecture_basic;

SELECT lecture_name FROM lecture_special;

SELECT lecture_name FROM lecture_basic UNION ALL SELECT lecture_name FROM lecture_special ORDER BY lecture_name ASC;