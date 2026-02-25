# 07_Exception_Handling_examples.py

# 1. Handling Division by Zero
print("--- Division Example ---")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: You cannot divide a number by zero.")

# 2. Handling Multiple Exceptions
print("\n--- Input Error Example ---")
try:
    # simulate user input
    user_input = "hello" 
    number = int(user_input)
except ValueError:
    print(f"Error: Could not convert '{user_input}' to an integer.")

# 3. Using Finally
print("\n--- Finally Example ---")
try:
    x = 10 / 2
    print("Result is:", x)
except:
    print("Something went wrong.")
finally:
    print("This block always runs (used for cleanup).")
