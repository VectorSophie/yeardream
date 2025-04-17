DESC LECTURE;
DESC LECTURE_TYPE;

SELECT type_id, type_name, 
(SELECT COUNT(*) FROM LECTURE AS l WHERE l.lecture_type_id = t.type_id)
FROM LECTURE_TYPE AS t ORDER BY type_id ASC;