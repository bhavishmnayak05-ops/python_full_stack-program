-- MySQL Fundamentals Practice Script
-- This script covers DDL, DML, DQL, Constraints, and Joins.

-- 1. DATABASE CREATION (DDL)
CREATE DATABASE IF NOT EXISTS practice_db;
USE practice_db;

-- 2. TABLE CREATION WITH CONSTRAINTS (DDL)
CREATE TABLE IF NOT EXISTS departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS employees (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    salary DECIMAL(10, 2) CHECK (salary > 0),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id) ON DELETE SET NULL
);

-- 3. INSERTING DATA (DML)
INSERT INTO departments (dept_id, dept_name) VALUES 
(1, 'Engineering'),
(2, 'Marketing'),
(3, 'Human Resources');

INSERT INTO employees (emp_id, first_name, last_name, email, salary, dept_id) VALUES 
(101, 'Arjun', 'Reddy', 'arjun@example.com', 75000.00, 1),
(102, 'Deepa', 'Nair', 'deepa@example.com', 65000.00, 1),
(103, 'Karan', 'Johar', 'karan@example.com', 55000.00, 2),
(104, 'Ishita', 'Dutta', 'ishita@example.com', 60000.00, 3),
(105, 'Suresh', 'Raina', 'suresh@example.com', 70000.00, NULL); -- No department

-- 4. BASIC QUERIES (DQL)
-- Select all
SELECT * FROM employees;

-- Filtered select
SELECT first_name, salary FROM employees WHERE salary > 60000;

-- Sorting
SELECT * FROM employees ORDER BY salary DESC;

-- Aggregation
SELECT AVG(salary) AS average_salary FROM employees;
SELECT dept_id, COUNT(*) AS employee_count FROM employees GROUP BY dept_id;

-- 5. UPDATING DATA (DML)
UPDATE employees SET salary = salary * 1.05 WHERE emp_id = 101;

-- 6. JOINS
-- Inner Join: Employees with their departments
SELECT e.first_name, d.dept_name 
FROM employees e 
INNER JOIN departments d ON e.dept_id = d.dept_id;

-- Left Join: All employees, including those without a department
SELECT e.first_name, d.dept_name 
FROM employees e 
LEFT JOIN departments d ON e.dept_id = d.dept_id;

-- Right Join: All departments, including those without employees
SELECT e.first_name, d.dept_name 
FROM employees e 
RIGHT JOIN departments d ON e.dept_id = d.dept_id;

-- 7. CLEANUP (Optional)
-- DROP TABLE employees;
-- DROP TABLE departments;
-- DROP DATABASE practice_db;
