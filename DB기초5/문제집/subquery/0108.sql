SELECT *, (SELECT (kor+eng+math)/3 FROM test as t WHERE s.id = t.id) AS
test_average
FROM students AS s;
