DESC REQUEST;
DESC REQUEST_DTL;

SELECT request_dtl_id, request_id, request_name, request_content FROM REQUEST_DTL WHERE request_id IN
(SELECT request_id FROM REQUEST WHERE request_status = 'FAILED');
ORDER BY request_dtl_id ASC;