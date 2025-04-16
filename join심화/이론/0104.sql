DESC LOGIN_HISTORY;
DESC MEMBER;

SELECT login_history_id, member_name, member_email, login_date FROM LOGIN_HISTORY NATURAL JOIN MEMBER ORDER BY login_history_id ASC;
