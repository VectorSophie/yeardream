DESC request_past;
DESC request_new;

SELECT name, number FROM request_past UNION ALL SELECT name, number FROM request_new ORDER BY name ASC;

SELECT name, number FROM request_past UNION SELECT name, number FROM request_new ORDER BY name ASC;