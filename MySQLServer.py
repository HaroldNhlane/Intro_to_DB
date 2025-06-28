import mysql.connector

# Replace with your connection details
# Initially connect without specifying a database, so we can create it if it doesn't exist
mydb = mysql.connector.connect(
    host="localhost",  # Or "127.0.0.1"
    port=3306,         # Specify the port separately
    user="root",
    password="xolani"
)

mycursor = mydb.cursor()

# 1. Create the database if it doesn't exist
try:
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' checked/created successfully.")
except mysql.connector.Error as err:
    print(f"Error creating database: {err}")
    # It's good practice to close if there's an error this early
    mycursor.close()
    mydb.close()
    exit() # Exit the script if database creation/check fails

# 2. Select the database for subsequent operations
mycursor.execute("USE alx_book_store")
print("Switched to database 'alx_book_store'.")

# Important: Create tables in the correct order due to foreign key dependencies

# 3. Create Authors table (no foreign keys, so it can be first)
mycursor.execute("""
CREATE TABLE IF NOT EXISTS Authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(255)
);
""")
print("Authors table created successfully.")

# 4. Create Customers table (no foreign keys, can be created early)
mycursor.execute("""
CREATE TABLE IF NOT EXISTS Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT
);
""")
print("Customers table created successfully.")

# 5. Create Books table (depends on Authors)
mycursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(130),
    author_id INT,
    price DOUBLE,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);
""")
print("Books table created successfully.")

# 6. Create Orders table (depends on Customers)
mycursor.execute("""
CREATE TABLE IF NOT EXISTS Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);
""")
print("Orders table created successfully.")

# 7. Create Order_Details table (depends on Orders and Books)
mycursor.execute("""
CREATE TABLE IF NOT EXISTS Order_Details (
    orderdetailid INT PRIMARY KEY,
    order_id INT,
    book_id INT,
    quantity DOUBLE,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);
""")
print("Order_Details table created successfully.")

# Close the cursor and connection
mycursor.close()
mydb.close()
print("Database connection closed.")