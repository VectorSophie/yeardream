DESC STORE;
DESC STORE_TYPE_CODE;

SELECT store_name, store_type_name FROM STORE INNER JOIN STORE_TYPE_CODE ON STORE.store_type_code = STORE_TYPE_CODE.store_type_code ORDER BY store_name ASC;
