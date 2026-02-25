# Topic 4: Functions and Modules

## 1. What is a Function?
A function is a block of code that only runs when it is called. You can pass data, known as parameters, into a function.

```python
# Defining a function
def greet(name):
    print("Hello, " + name)

# Calling a function
greet("Sriram")
```

## 2. Return Values
Functions can return a result using the `return` keyword.

```python
def add(a, b):
    return a + b

result = add(5, 10)
print(result) # Output: 15
```

## 3. Modules
A module is a file containing Python code (functions, variables). You can use built-in modules using the `import` keyword.

```python
import math
print(math.sqrt(16)) # Output: 4.0
```
