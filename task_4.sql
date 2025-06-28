-- task_4.sql

-- Prints the full description of the 'books' table
-- from the database 'alx_book_store' using INFORMATION_SCHEMA.
-- The database name will be passed as an argument to the mysql command.
-- DESCRIBE and EXPLAIN statements are not allowed.

SELECT
    COLUMN_NAME AS FIELD,
    COLUMN_TYPE AS TYPE,
    IS_NULLABLE AS 'NULL',
    COLUMN_KEY AS KEY,
    COLUMN_DEFAULT AS DEFAULT,
    EXTRA
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_SCHEMA = 'ALX_BOOK_STORE' AND TABLE_NAME = 'BOOKS'
ORDER BY
    ORDINAL_POSITION;