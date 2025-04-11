ALTER TABLE bookstore MODIFY name VARCHAR(50) NOT NULL;
ALTER TABLE bookstore ALTER author SET DEFAULT '홍길동';
ALTER TABLE bookstore ADD CONSTRAINT checker CHECK (price > 0);


