-- task_6.sql

-- Inserts multiple rows into the 'customers' table in the 'alx_book_store' database.
-- The database name will be passed as an argument to the MySQL command.

INSERT INTO customer (customer_id, customer_name, emailL, address) VALUES
((2, 'Blessing Malik', 'bmalik@sandtech.com', '124 Happiness  Ave.'),
(3, 'Obed Ehoneah', 'eobed@sandtech.com', '125 Happiness  Ave.'),
(4, 'Nehemial Kamolu', 'nkamolu@sandtech.com', '126 Happiness  Ave.');