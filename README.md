Task 1 — Create a database and table
Create a SQLite database called shop.db.

Create a table products with:

id — integer, primary key
name — text, required
price — real, required
quantity — integer, default 0
Restrictions:

Use Python's built-in sqlite3 module.
The table should be created automatically when the script starts.
Task 2 — Insert products
Add 5 different products to the products table.

Example products:

Laptop       1200.00
Mouse          25.50
Keyboard       70.00
Monitor       300.00
Headphones     80.00
Restrictions:

Use INSERT.
Use SQL parameters (?) instead of putting values directly into the SQL string.
Insert all 5 products from Python.
Task 3 — Display all products
Write a Python function:

get_all_products()
It should return and print all products from the database.

Expected output:

1 Laptop 1200.0 5
2 Mouse 25.5 20
...


Task 4 — Find products by price
Write a function:

get_products_cheaper_than(price)
It should display all products cheaper than the specified price.

Example:

get_products_cheaper_than(100)
Task 5 — Update a product
Write a function:

update_price(product_id, new_price)
It should change the price of one product.

Example:

update_price(2, 30.00)
Task 6 — Delete a product
Write a function:

delete_product(product_id)
It should delete one product by ID.

Example:

delete_product(3)
Task 7 — Calculate total stock value
Calculate how much money all products currently represent.

For example:

Laptop      1200 × 5  = 6000
Mouse         25 × 20 = 500
Keyboard      70 × 10 = 700

Total = 7200
Restrictions:

Do it using SQL, not by calculating everything in Python.
Use:
SUM(...)
Create a function:
get_total_stock_value()
