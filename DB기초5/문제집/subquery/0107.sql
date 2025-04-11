SELECT user_id, date, country
FROM ticket t
INNER JOIN airplane a ON t.airplane_id = a.id
AND country NOT IN('Korea', 'China', 'Japan')
ORDER BY user_id ASC;