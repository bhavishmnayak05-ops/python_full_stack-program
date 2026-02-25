# Topic 8: File Handling (Basics)

Python allows you to read from and write to files using the `open()` function.

## 1. Opening a File
Syntax: `file = open("filename", "mode")`

### Common Modes:
- **'r'**: Read (default). Opens for reading.
- **'w'**: Write. Creates a new file or overwrites an existing one.
- **'a'**: Append. Adds data to the end of an existing file.

## 2. Using `with` Statement (Recommended)
The `with` statement automatically closes the file for you.

```python
# Writing to a file
with open("test.txt", "w") as f:
    f.write("Hello Python!")

# Reading from a file
with open("test.txt", "r") as f:
    content = f.read()
    print(content)
```
