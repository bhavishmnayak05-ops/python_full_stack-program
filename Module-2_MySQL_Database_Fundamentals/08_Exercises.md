# 08. Exercises - MySQL Fundamentals

Apply what you've learned through these practical exercises.

## Task 1: Database Setup (DDL)
1. Create a database named `ecommerce_db`.
2. Create a table `products` with the following columns:
    - `id` (INT, Primary Key)
    - `name` (VARCHAR, Not Null)
    - `price` (DECIMAL, Check > 0)
    - `category` (VARCHAR, Default 'General')
3. Alter the table to add a `stock_quantity` column.

## Task 2: Data Entry (DML)
1. Insert 5 different products into the `products` table.
2. Update the price of one product by 10%.
3. Delete any product that has a stock quantity of 0.

## Task 3: Querying Data (DQL)
1. Select all products in the 'Electronics' category.
2. Select names and prices of products, sorted by price in descending order.
3. Find the average price of all products.
4. Count how many products are in each category using `GROUP BY`.

## Task 4: Relationships and Joins
1. Create a `customers` table and an `orders` table.
2. Link them using a Foreign Key (`customer_id`).
3. Write a query to find the names of customers along with the dates of their orders using an `INNER JOIN`.
4. Write a query to show all customers, even those who haven't placed an order, using a `LEFT JOIN`.

## Challenge Project
Design a simple "Library Management System" schema.
- Define tables for `Books`, `Authors`, and `Borrowers`.
- Establish relationships (e.g., Many-to-One from Books to Authors).
- Create a list of all books along with their author names.
