# Topic 7: Exception Handling

Exceptions are errors that happen during program execution. Python uses `try`, `except`, `finally` to handle them without crashing the program.

## 1. The Try-Except Block
```python
try:
    # Code that might cause an error
    x = 10 / 0
except ZeroDivisionError:
    # Code to run if error happens
    print("Cannot divide by zero!")
```

## 2. Using `else` and `finally`
- **else:** Runs if NO exception occurs.
- **finally:** ALWAYS runs, whether there was an error or not.

```python
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That's not a number!")
finally:
    print("Execution complete.")
```
