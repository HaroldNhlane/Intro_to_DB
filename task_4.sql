-- task_4.sql
-- This script shows the full description of the books table without using DESCRIBE or EXPLAIN
SELECT 
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_NAME = 'books'
    AND TABLE_SCHEMA = 'alx_book_store';
