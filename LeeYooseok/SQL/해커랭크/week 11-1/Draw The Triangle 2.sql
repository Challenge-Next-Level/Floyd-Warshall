SET @num = 0;
SELECT REPEAT('* ', @num := @num + 1)
FROM information_schema.TABLES
LIMIT 20;
