CREATE TABLE customer(
    customer_number VARCHAR(10) PRIMARY KEY,
    name VARCHAR(10) NOT NULL,
    id VARCHAR(15) NOT NULL UNIQUE,
    pw VARCHAR(20) NOT NULL,
    phone_number VARCHAR(11),
    birth_date DATE
);

CREATE TABLE brand(
    brand_number INT PRIMARY KEY,
    name VARCHAR(20) NOT NULL UNIQUE,
    company VARCHAR(20) NOT NULL
);

CREATE TABLE kickboard(
    id VARCHAR(4) PRIMARY KEY,
    brand_number INT NOT NULL,
    model_year INT NOT NULL,
    basic_price INT NOT NULL,
    price_per_minute INT NOT NULL,
    FOREIGN KEY (brand_number) REFERENCES brand(brand_number)
);

CREATE TABLE borrow(
    customer_number VARCHAR(10),
    rental_time DATETIME,
    lat_location FLOAT NOT NULL,
    lon_location FLOAT NOT NULL,
    rental_status ENUM('대여', '반납') NOT NULL,
    kickboard_id VARCHAR(4) NOT NULL,
    CONSTRAINT borrow_pk PRIMARY KEY (customer_number, rental_time),
    FOREIGN KEY (customer_number) REFERENCES customer(customer_number),
    FOREIGN KEY (kickboard_id) REFERENCES kickboard(id)
);

SELECT * FROM information_schema.table_constraints WHERE CONSTRAINT_TYPE = 'FOREIGN KEY';
DESC customer;
DESC brand;
DESC kickboard;
DESC borrow;