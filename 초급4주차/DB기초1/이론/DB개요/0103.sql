DESC kickboards;

ALTER TABLE kickboards ADD COLUMN member_birthday DATE NULL;

ALTER TABLE kickboards MODIFY COLUMN rental_date TIME NULL;

ALTER TABLE kickboards MODIFY COLUMN member_id VARCHAR(16) NOT NULL;
ALTER TABLE kickboards MODIFY COLUMN kickboard_id VARCHAR(16) NOT NULL;

ALTER TABLE kickboards CHANGE COLUMN kickboard_id id VARCHAR(16) NOT NULL;
ALTER TABLE kickboards CHANGE COLUMN kickboard_brand brand VARCHAR(16) NULL;

ALTER TABLE kickboards DROP COLUMN distance;

ALTER TABLE kickboards RENAME kickboard;

DESC kickboard;