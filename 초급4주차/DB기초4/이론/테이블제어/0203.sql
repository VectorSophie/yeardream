DESC rental;

SELECT user_id, COUNT(*) FROM rental GROUP BY user_id HAVING COUNT(user_id) > 1;