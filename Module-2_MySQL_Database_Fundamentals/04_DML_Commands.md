# 04. SQL Commands - DML (Data Manipulation Language)

DML commands allow you to modify the data stored within your tables. Unlike DDL, which deals with structure, DML deals with the content.

## 1. INSERT
Used to add new rows of data into a table.

### Inserting a Single Record:
```sql
INSERT INTO students (student_id, first_name, last_name, email) 
VALUES (101, 'Rahul', 'Sharma', 'rahul@example.com');
```

### Inserting Multiple Records:
```sql
INSERT INTO students (student_id, first_name, last_name, email) 
VALUES 
(102, 'Priya', 'Verma', 'priya@example.com'),
(103, 'Amit', 'Kumar', 'amit@example.com'),
(104, 'Sneha', 'Gupta', 'sneha@example.com');
```

## 2. UPDATE
Used to modify existing data in a table. 

> [!WARNING]
> Always use a `WHERE` clause with `UPDATE`. If you omit it, every single row in the table will be updated!

### Example:
```sql
-- Update email for a specific student
UPDATE students 
SET email = 'rahul.new@example.com' 
WHERE student_id = 101;

-- Update multiple columns
UPDATE students 
SET first_name = 'Amitabh', last_name = 'Bachchan' 
WHERE student_id = 103;
```

## 3. DELETE
Used to remove records from a table.

> [!WARNING]
> Always use a `WHERE` clause with `DELETE`. If you omit it, all records will be deleted, though the table structure will remain (similar to `TRUNCATE`).

### Example:
```sql
-- Delete a specific record
DELETE FROM students WHERE student_id = 104;

-- Delete records based on a condition
DELETE FROM students WHERE email LIKE '%@oldmail.com';
```

## DELETE vs. TRUNCATE
| Feature | DELETE | TRUNCATE |
| :--- | :--- | :--- |
| **Type** | DML | DDL |
| **Filters** | Can use `WHERE` | Cannot use `WHERE` |
| **Speed** | Slower (deletes row by row) | Faster (resets the table) |
| **Rollback** | Can be rolled back | Cannot be rolled back |

## Summary
DML commands (`INSERT`, `UPDATE`, `DELETE`) are the core of day-to-day database operations. Mastering them is essential for any developer working with data.
