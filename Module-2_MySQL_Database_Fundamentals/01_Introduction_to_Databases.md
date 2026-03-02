# 01. Introduction to Databases & RDBMS

## What is a Database?
A **Database** is an organized collection of structured information, or data, typically stored electronically in a computer system. A database is usually controlled by a **Database Management System (DBMS)**. 

### Why do we need Databases?
In the early days of computing, data was stored in flat files (txt, csv). However, as data grew, several problems emerged:
- **Data Redundancy:** Same data stored in multiple places.
- **Data Inconsistency:** Updates in one place might not reflect in another.
- **Security Issues:** Difficult to control who can access what.
- **Scaling:** Poor performance when searching through millions of lines.

## What is an RDBMS?
**RDBMS** stands for **Relational Database Management System**. It is a type of DBMS that stores data in a structured format, using rows and columns. 

### Key Concepts:
1.  **Table:** A collection of related data entries consisting of columns and rows.
2.  **Record (Row):** A single, implicit structured data item in a table.
3.  **Field (Column):** A set of data values of a particular simple type, one for each row of the table.
4.  **Schema:** The formal structure of the database, defining how data is organized into tables.

### The Relational Model
The "Relational" part means that data in different tables can be related to each other using common keys (like IDs).

## MySQL Overview
**MySQL** is the world's most popular open-source relational database management system. 

### Why use MySQL?
- **Open Source:** It's free to use and has a massive community.
- **High Performance:** Quick and reliable for web applications.
- **Scalability:** Can handle massive amounts of data and high-traffic websites (used by Facebook, YouTube, Netflix).
- **Security:** Features top-notch data security layers.

## SQL vs. NoSQL
| Feature | SQL (Relational) | NoSQL (Non-Relational) |
| :--- | :--- | :--- |
| **Structure** | Tabular (Rows & Columns) | Document, Key-Value, Graph |
| **Schema** | Pre-defined (Fixed) | Dynamic (Flexible) |
| **Scaling** | Vertically (Bigger Server) | Horizontally (More Servers) |
| **Examples** | MySQL, PostgreSQL, Oracle | MongoDB, Cassandra, Redis |

## Summary
Understanding the difference between a simple database and a relational system is crucial. MySQL provides a robust, scalable, and secure environment to manage relational data using **SQL (Structured Query Language)**.
