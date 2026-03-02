# 07. Joins in SQL

Joins are used to combine rows from two or more tables, based on a related column between them. This is the heart of relational database queries.

## 1. INNER JOIN
Returns records that have matching values in both tables.

```sql
SELECT students.first_name, courses.course_name
FROM students
INNER JOIN enrollments ON students.student_id = enrollments.student_id
INNER JOIN courses ON enrollments.course_id = courses.course_id;
```

## 2. LEFT (OUTER) JOIN
Returns all records from the left table, and the matched records from the right table. If there is no match, the result is NULL from the right side.

```sql
-- Show all students and their courses (even if they aren't enrolled in any)
SELECT students.first_name, courses.course_name
FROM students
LEFT JOIN enrollments ON students.student_id = enrollments.student_id
LEFT JOIN courses ON enrollments.course_id = courses.course_id;
```

## 3. RIGHT (OUTER) JOIN
Returns all records from the right table, and the matched records from the left table. If there is no match, the result is NULL from the left side.

```sql
-- Show all courses and any students enrolled in them
SELECT students.first_name, courses.course_name
FROM students
RIGHT JOIN enrollments ON students.student_id = enrollments.student_id
RIGHT JOIN courses ON enrollments.course_id = courses.course_id;
```

## 4. CROSS JOIN
Returns the Cartesian product of the two tables (every row of the first table joined with every row of the second table).

```sql
SELECT students.first_name, courses.course_name
FROM students
CROSS JOIN courses;
```

## 5. SELF JOIN
A self join is a regular join, but the table is joined with itself. This is useful for hierarchical data (like an employee table with a `manager_id` column).

```sql
SELECT A.name AS Employee, B.name AS Manager
FROM employees A, employees B
WHERE A.manager_id = B.id;
```

## Understanding Join Types (Venn Diagram Concept)
- **Inner Join:** Intersection of A and B.
- **Left Join:** Everything in A, plus the intersection with B.
- **Right Join:** Everything in B, plus the intersection with A.
- **Full Join (MySQL Shortcut):** MySQL doesn't have a `FULL OUTER JOIN`, but you can achieve it by using `UNION` on a `LEFT JOIN` and a `RIGHT JOIN`.

## Summary
Joins allow you to normalize your database into smaller, specialized tables and then recombine that data on-the-fly to generate complex reports.
