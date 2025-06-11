CREATE TABLE customer(
    customer_number VARCHAR(10) PRIMARY KEY,
    name VARCHAR(10) NOT NULL,
    id VARCHAR(15) NOT NULL UNIQUE,
    pw VARCHAR(20) NOT NULL,
    phone_number VARCHAR(11),
    birth_date DATE
);

CREATE TABLE kickboard(
    id VARCHAR(10) PRIMARY KEY,
    brand VARCHAR(20) NOT NULL,
    model_year INT NOT NULL,
    price_per_minute INT NOT NULL,
    basic_price INT NOT NULL,
    company VARCHAR(20) NOT NULL
);

DESC customer;
DESC kickboard;

INSERT INTO customer
VALUES('0187642351', '김민준', 'kmax6', 'HASH-lui235dfi2', '08786173448', '1989-03-09');
INSERT INTO kickboard
VALUES('7YWC', 'boardkick', 2015, 100, 1000, 'elice');