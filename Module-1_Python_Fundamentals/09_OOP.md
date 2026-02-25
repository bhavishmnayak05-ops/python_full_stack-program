# Topic 9: Object-Oriented Programming (OOP)

OOP is a way of organizing code by creating "objects" that contain data and functions.

## 1. Class and Object
- **Class:** A blueprint for creating objects (e.g., "Car").
- **Object:** An instance of a class (e.g., "Your Toyota").

## 2. The 4 Pillars of OOP

### A. Encapsulation
Encapsulation means wrapping data (variables) and methods (functions) into a single unit (class). It also involves restricting direct access to data to prevent accidental modification.
- **Private variables:** Use double underscore `__` to make a variable private.

### B. Inheritance
Inheritance allows a "Child" class to reuse the code of a "Parent" class. This helps in code reusability.
- **Syntax:** `class ChildClass(ParentClass):`

### C. Polymorphism
Polymorphism allows different classes to have methods with the same name but different behaviors. This is usually done through **Method Overriding**.

### D. Abstraction
Abstraction means hiding complex implementation details and showing only the necessary features. In Python, we use the `abc` module to create **Abstract Classes**. An abstract class cannot be instantiated directly and forces child classes to implement specific methods.
