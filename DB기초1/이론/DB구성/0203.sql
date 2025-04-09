CREATE TABLE kickboard(
    member_id       VARCHAR(16)  NOT NULL UNIQUE,
    member_name     VARCHAR(16)  NOT NULL,
    member_birthday DATE,
    id              VARCHAR(16)  PRIMARY KEY,
    brand           VARCHAR(16)  NOT NULL,   
    rental_location VARCHAR(32)  NOT NULL,
    rental_time     TIME, 
    price           INT          DEFAULT 1000,
    CONSTRAINT id_unique UNIQUE (id),
    CONSTRAINT member_birthday_check CHECK (member_birthday < '2000-01-01')
);

DESC kickboard;

INSERT INTO kickboard(member_id, member_name, member_birthday, brand, rental_location, rental_time, price)
VALUES('kmax6', '김민준', '1989-03-09', 'boardkick', '서울시 관악구 신림동', '00:05:25', 4700);