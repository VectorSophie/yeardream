SELECT * FROM shareholder;
SELECT * FROM shareholder WHERE stock >= 100000;
SELECT stock FROM shareholder WHERE name IN ("Alexis", "Craig",
"Fred");
SELECT name,stock FROM shareholder WHERE agree = 0 AND stock >= 100000;
SELECT name,stock FROM shareholder WHERE agree = 1 AND stock >= 100000;
SELECT * FROM shareholder WHERE stock <= 100000 OR stock >= 200000;
