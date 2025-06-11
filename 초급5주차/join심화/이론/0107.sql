DESC RESPONSE_DTL;
DESC REQUEST;

SELECT request_id, request_member_id, response_content FROM RESPONSE_DTL RIGHT OUTER JOIN REQUEST ON RESPONSE_DTL.response_id = REQUEST.response_id ORDER BY request_id ASC;