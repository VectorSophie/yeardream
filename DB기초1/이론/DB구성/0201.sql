CREATE TABLE kickboard(
    member_id       VARCHAR(16) NOT NULL,
    member_name     VARCHAR(16) NOT NULL,
    member_birthday DATE CHECK(member_birthday < '2000-01-01'),
    id              VARCHAR(16) NOT NULL UNIQUE,
    brand           VARCHAR(16) NOT NULL,   
    rental_location VARCHAR(32) NOT NULL,
    rental_time     TIME CHECK(rental_time < '01:00:00'), 
    price           INT DEFAULT 0
);

INSERT INTO kickboard(member_id, member_name, member_birthday, id, brand, rental_location, rental_time, price)
VALUES('kmax6', '김민준', '2000-01-01', '7YWC', 'boardkick', '서울시 관악구 신림동', '00:05:25', 4700);
INSERT INTO kickboard(member_id, member_name, member_birthday, id, brand, rental_location, rental_time, price)
VALUES('flykite', '이서연', '1999-01-01', 'JXAN', 'willgo', '서울시 동작구 대방동', '01:09:00', 7200);