SELECT MEMBER.member_id, member_name, member_grade FROM MEMBER LEFT OUTER JOIN MEMBER_DTL ON MEMBER.member_id = MEMBER_DTL.member_id ORDER BY member_id;

SELECT MEMBER.member_id, member_name, member_grade FROM MEMBER LEFT OUTER JOIN MEMBER_DTL ON MEMBER.member_id = MEMBER_DTL.member_id WHERE member_grade IS NULL OR member_grade = 'BRONZE' ORDER BY member_id ORDER BY member_id;