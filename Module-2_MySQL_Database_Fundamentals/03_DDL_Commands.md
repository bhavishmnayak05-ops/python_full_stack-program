# 03. SQL Commands - DDL (Data Definition Language)

DDL commands are used to define or modify the structure of the database. These changes are permanent (auto-committed).

## 1. CREATE
Used to create a new database or table.

### Creating a Database:
```sql
CREATE DATABASE school_db;
-- To use the database
USE school_db;
```

### Creating a Table:
```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    admission_date DATE
);
```

## 2. ALTER
Used to modify the structure of an existing table.

### Adding a Column:
```sql
ALTER TABLE students ADD phone_number VARCHAR(15);
```

### Modifying Column Data Type:
```sql
ALTER TABLE students MODIFY phone_number VARCHAR(20);
```

### Dropping a Column:
```sql
ALTER TABLE students DROP COLUMN last_name;
```

### Renaming a Column:
```sql
ALTER TABLE students RENAME COLUMN first_name TO name;
```

## 3. DROP
Used to delete a database or a table permanently. Caution: This removes data and structure.

```sql
DROP TABLE students;
DROP DATABASE school_db;
```

## 4. TRUNCATE
Used to remove all records from a table, but the table structure (schema) remains. It is faster than `DELETE`.

```sql
TRUNCATE TABLE students;
```

## 5. RENAME
Used to rename a table.

```sql
RENAME TABLE students TO student_records;
```

## Summary
DDL focuses on the "Container" (Database/Table) rather than the "Content" (Data). Use these commands when you need to change the blueprint of your data storage.
