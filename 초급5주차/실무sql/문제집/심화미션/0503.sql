WITH RECURSIVE CTE(mentee_id, mento_id, lvl)
AS (
SELECT mentee_id, mento_id, 0 AS lvl
FROM MEMBER
WHERE mento_id IS NULL
UNION ALL
SELECT a.mentee_id, a.mento_id, b.lvl + 1
FROM MEMBER a
JOIN CTE AS b
ON a.mento_id = b.mentee_id
)
SELECT mentee_id, mento_id, lvl
FROM CTE
ORDER BY lvl, mentee_id;
