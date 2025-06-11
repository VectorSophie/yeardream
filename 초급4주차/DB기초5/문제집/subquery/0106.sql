SELECT user_id, date, time
FROM ticket
WHERE date BETWEEN '2019-10-01' AND '2019-12-31'
AND country = 'Korea';
