INSERT INTO customer VALUES('0187642351', '김민준', 'kmax6', 'HASH-lui235dfi2', '08786173448', '1989-03-09');
INSERT INTO customer VALUES('0012616925', '이서연', 'flykite', 'HASH-u73ylz5jao', '21865059766', '1995-07-12');

INSERT INTO brand VALUES(100, 'boardkick', 'elice');
INSERT INTO brand VALUES(200, 'willgo', 'everythere');
INSERT INTO brand VALUES(201, 'fastgoing', 'everythere');

INSERT INTO kickboard VALUES('7YWC', 100, 2015, 1000, 100);
INSERT INTO kickboard VALUES('54JP', 100, 2015, 1000, 100);
INSERT INTO kickboard VALUES('672Z', 200, 2018, 950, 110);
INSERT INTO kickboard VALUES('7L3D', 100, 2018, 1050, 100);

INSERT INTO borrow VALUES('0187642351', '2020-08-20 13:01:02', 37.514194, 127.065038, '대여', '7YWC');
INSERT INTO borrow VALUES('0187642351', '2020-08-20 13:12:32', 37.5141, 127.0600, '반납', '7YWC');
INSERT INTO borrow VALUES('0187642351', '2020-09-01 20:39:52', 37.4664, 126.931, '대여', '672Z');
INSERT INTO borrow VALUES('0187642351', '2020-09-01 20:48:55', 37.4694, 126.9449, '반납', '672Z');
INSERT INTO borrow VALUES('0012616925', '2020-11-11 22:01:30', 36.6638, 127.5013, '대여', '7L3D');
INSERT INTO borrow VALUES('0012616925', '2020-11-11 22:16:50', 36.6372, 127.4904, '반납', '7L3D');