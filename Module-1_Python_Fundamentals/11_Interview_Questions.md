# Module 1: Top Interview Questions

Prepare for your interviews with these common questions based on Python fundamentals.

## Basic Questions
1. **What is Python? What are its key features?**
   - *Answer:* Python is a high-level, interpreted, general-purpose programming language. Features include readability, large libraries, and being dynamically typed.

2. **What is the difference between a List and a Tuple?**
   - *Answer:* Lists are mutable (can be changed) and defined with `[]`. Tuples are immutable (cannot be changed) and defined with `()`.

3. **What are PEP 8 and why is it important?**
   - *Answer:* PEP 8 is Python's style guide. it helps keep code consistent and readable.

4. **How is memory managed in Python?**
   - *Answer:* Memory is managed automatically via a private heap space and a Garbage Collector.

## Data Types and Structures
5. **What is a dictionary in Python?**
   - *Answer:* A collection of unordered (or ordered since 3.7), changeable, and indexed key-value pairs.

6. **How do you remove duplicates from a list?**
   - *Answer:* By converting the list into a `set()`, as sets do not allow duplicates. Example: `list(set(my_list))`.

7. **What is the difference between `break`, `continue`, and `pass`?**
   - *Answer:* `break` exits the loop. `continue` skips the current iteration. `pass` is a null statement used as a placeholder.

## Functions and Modules
8. **What is the `self` keyword in Python?**
   - *Answer:* `self` refers to the instance of the class. It allows access to the attributes and methods of the class in Python.

9. **What is the difference between built-in modules and custom modules?**
   - *Answer:* Built-in modules come with Python (like `math`, `os`). Custom modules are files created by the user containing Python code.

## OOP Principles
10. **Explain the 4 Pillars of OOP in Python.**
    - *Answer:* Encapsulation (hiding data), Inheritance (reusing code), Polymorphism (multiple forms), and Abstraction (hiding implementation).

11. **What is a constructor in Python?**
    - *Answer:* The `__init__` method is the constructor, used to initialize an object's attributes when the object is created.

12. **What is the `super()` function?**
    - *Answer:* It is used to call methods from the parent class inside a child class.

## Error and File Handling 
13. **What is the purpose of the `finally` block?**
    - *Answer:* It contains code that must execute regardless of whether an exception occurred or not (used for cleanup).

14. **What is the difference between 'w' and 'a' modes in file handling?**
    - *Answer:* 'w' (write) overwrites the file. 'a' (append) adds content to the end of the existing file.
