DESC customer;
DESC borrow;

DROP TABLE borrow;

CREATE TABLE company(
    brand VARCHAR(20) PRIMARY KEY,
    price_per_minute INT NOT NULL,
    name VARCHAR(20) NOT NULL
);

CREATE TABLE price(
    brand VARCHAR(20) NOT NULL,
    model_year INT NOT NULL,
    basic_price INT NOT NULL,
    CONSTRAINT price_pk PRIMARY KEY(brand, model_year), FOREIGN KEY(brand) REFERENCES company(brand)
);

CREATE TABLE borrow(
    customer_id VARCHAR(5) NOT NULL,
    rental_time DATETIME NOT NULL,
    rental_location VARCHAR(20) NOT NULL,
    brand VARCHAR(20) NOT NULL,
    model_year INT NOT NULL,
    CONSTRAINT borrow_pk PRIMARY KEY(customer_id, rental_time), FOREIGN KEY(customer_id) REFERENCES customer(customer_id), FOREIGN KEY (brand, model_year) REFERENCES price(brand, model_year)
);

SELECT * FROM information_schema.table_constraints WHERE CONSTRAINT_TYPE = 'FOREIGN KEY';
DESC company;
DESC price;
DESC borrow;
