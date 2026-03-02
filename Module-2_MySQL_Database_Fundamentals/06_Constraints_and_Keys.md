# 06. Constraints and Keys

Constraints are rules applied to columns in a table to ensure the accuracy and reliability of the data.

## 1. Common Constraints
-   **NOT NULL:** Ensures that a column cannot have a NULL value.
-   **UNIQUE:** Ensures that all values in a column are different.
-   **CHECK:** Ensures that the values in a column satisfy a specific condition.
-   **DEFAULT:** Sets a default value for a column if no value is specified.

```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT CHECK (age >= 18),
    country VARCHAR(50) DEFAULT 'India'
);
```

## 2. Primary Key (PK)
A **Primary Key** is a field in a table which uniquely identifies each row/record in a database table.
- A table can have only **one** primary key.
- It cannot contain NULL values.
- It must be unique.

```sql
ALTER TABLE students ADD PRIMARY KEY (student_id);
```

## 3. Foreign Key (FK)
A **Foreign Key** is a column or group of columns in a relational database table that provides a link between data in two tables. It acts as a cross-reference between tables because it references the primary key of another table.

### Establishing a Relationship:
```sql
CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100)
);

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
```

## 4. Referential Integrity
This concept ensures that relationships between tables remain consistent. For example, you shouldn't be able to delete a student who is currently enrolled in a course unless you handle the enrollment record first.

### ON DELETE CASCADE
Automatically deletes the child records when the parent record is deleted.
```sql
FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
```

## Summary
Keys and constraints form the backbone of a relational database. They prevent dirty data from entering the system and maintain the integrity of linked information.
