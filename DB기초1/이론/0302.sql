DESC customer;

DROP TABLE customer;

CREATE TABLE customer(
    customer_id VARCHAR(5) NOT NULL PRIMARY KEY,
    customer_name VARCHAR(10) NOT NULL
);

CREATE TABLE borrow(
    customer_id VARCHAR(5) NOT NULL,
    rental_time DATETIME NOT NULL,
    rental_location VARCHAR(20) NOT NULL,
    brand VARCHAR(20) NOT NULL,
    model_year INT NOT NULL,
    price_per_minute INT NOT NULL,
    basic_price INT NOT NULL,
    company VARCHAR(20) NOT NULL,
    CONSTRAINT borrow_pk PRIMARY KEY(customer_id, rental_time), FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
);

SELECT * FROM information_schema.table_constraints WHERE CONSTRAINT_TYPE = 'FOREIGN KEY';
DESC customer;
DESC borrow;