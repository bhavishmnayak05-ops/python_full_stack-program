# 05. SQL Commands - DQL (Data Query Language)

DQL is used to retrieve data from the database. The primary command for DQL is `SELECT`.

## 1. SELECT Basics
The `SELECT` statement is used to fetch data from one or more tables.

```sql
-- Select all columns
SELECT * FROM students;

-- Select specific columns
SELECT first_name, email FROM students;
```

## 2. Filtering with WHERE
The `WHERE` clause is used to extract only those records that fulfill a specified condition.

```sql
-- Comparison Operators (=, <, >, <=, >=, !=)
SELECT * FROM students WHERE student_id = 101;

-- Logical Operators (AND, OR, NOT)
SELECT * FROM students WHERE student_id > 100 AND first_name = 'Rahul';

-- BETWEEN, IN, LIKE
SELECT * FROM students WHERE student_id BETWEEN 101 AND 103;
SELECT * FROM students WHERE first_name IN ('Rahul', 'Priya');
SELECT * FROM students WHERE email LIKE '%@example.com'; -- Wildcard search
```

## 3. Sorting with ORDER BY
Used to sort the result-set in ascending or descending order.

```sql
-- Ascending (default)
SELECT * FROM students ORDER BY first_name;

-- Descending
SELECT * FROM students ORDER BY admission_date DESC;
```

## 4. Aggregate Functions
Used to perform calculations on a set of values.
- `COUNT()`: Returns the number of rows.
- `SUM()`: Returns the total sum.
- `AVG()`: Returns the average value.
- `MIN()`: Returns the smallest value.
- `MAX()`: Returns the largest value.

```sql
SELECT COUNT(*) FROM students;
SELECT MAX(student_id) FROM students;
```

## 5. GROUP BY and HAVING
`GROUP BY` groups rows that have the same values into summary rows. `HAVING` is like `WHERE` but for groups.

```sql
-- Count students admitted on each date
SELECT admission_date, COUNT(*) 
FROM students 
GROUP BY admission_date;

-- Only show dates where more than 5 students were admitted
SELECT admission_date, COUNT(*) 
FROM students 
GROUP BY admission_date 
HAVING COUNT(*) > 5;
```

## Summary
DQL is the most frequently used part of SQL. It allows you to transform raw data into meaningful information by filtering, sorting, and aggregating.
