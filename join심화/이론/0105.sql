DESC FIRST_NAME_T;
DESC LAST_NAME_T;

SELECT first_name, last_name FROM FIRST_NAME_T CROSS JOIN LAST_NAME_T ORDER BY first_name ASC, last_name ASC;
