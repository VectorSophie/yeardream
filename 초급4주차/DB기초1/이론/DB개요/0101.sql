CREATE TABLE kickboard(
    member_id VARCHAR(16),
    member_name VARCHAR(16),
    kickboard_id VARCHAR(16),
    kickboard_brand VARCHAR(16),
    rental_location VARCHAR(32),
    rental_date DATETIME,
    distance INT,
    price INT
);

SHOW TABLES;

DESC kickboard;