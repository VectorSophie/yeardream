CREATE TABLE borrow(
    customer_number VARCHAR(10),
    rental_time DATETIME,
    rental_status ENUM('대여', '반납') NOT NULL,
    rental_location VARCHAR(20) NOT NULL,
    kickboard_id VARCHAR(10),
    CONSTRAINT borrow_pk PRIMARY KEY(customer_number, rental_time), FOREIGN KEY(customer_number) REFERENCES customer(customer_number), FOREIGN KEY (kickboard_id) REFERENCES kickboard(id)
);

SELECT * FROM information_schema.table_constraints WHERE CONSTRAINT_TYPE = 'FOREIGN KEY';
DESC borrow;

INSERT INTO customer
VALUES('0187642351', '김민준', 'kmax6', 'HASH-lui235dfi2', '08786173448', '1989-03-09');
INSERT INTO kickboard
VALUES('7YWC', 'boardkick', 2015, 100, 1000, 'elice');
INSERT INTO borrow
VALUES('0187642351', '2020-08-20 13:01:02', '대여', '서울시 강남구 역삼동', '7YWC');

