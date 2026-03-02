# 09. Interview Questions - MySQL Fundamentals

Prepare for your technical rounds with these common MySQL interview questions.

## Basic Level
1. **What is the difference between DBMS and RDBMS?**
2. **What is SQL? Is it the same as MySQL?**
3. **What are the different types of SQL commands? (DDL, DML, DQL, DCL, TCL)**
4. **What is a Primary Key? Can it be NULL?**
5. **What is a Unique Key? How is it different from a Primary Key?**

## Intermediate Level
6. **What is a Foreign Key? What is its purpose?**
7. **Explain the difference between DELETE and TRUNCATE.**
8. **What is a JOIN? Explain the different types of JOINs.**
9. **How do you handle NULL values in MySQL?**
10. **What is the purpose of the GROUP BY clause?**
11. **What is the difference between WHERE and HAVING?**
12. **What is an Aggregate Function? Give examples.**

## Advanced & Performance
13. **What is Normalization? Explain 1NF, 2NF, and 3NF.**
14. **What is an Index? How does it improve performance?**
15. **What is a View in MySQL?**
16. **Explain ACID properties in Databases.**
17. **What is a Stored Procedure?**
18. **What are Triggers?**
19. **How do you find the second-highest salary from an Employee table?**
    - `SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees);`
20. **What is a subquery?**

## Scenario-Based
21. **When would you use a LEFT JOIN instead of an INNER JOIN?**
22. **If you delete a parent record, what happens to the child record linked by a Foreign Key?**
23. **How do you prevent SQL Injection?**
24. **Why would you choose NoSQL over SQL for a project?**
25. **How do you export and import a MySQL database?**

---
**Tip:** When answering, always try to provide a small code snippet to illustrate your point. Practical experience is highly valued in interviews!
