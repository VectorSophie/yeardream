DESC REQUEST_HIST;
DESC MEMBER;

SELECT request_id, req_status, member_name FROM REQUEST_HIST INNER JOIN MEMBER ON REQUEST_HIST.req_member_id = MEMBER.member_id WHERE req_status = 'fail' ORDER BY request_id ASC;

