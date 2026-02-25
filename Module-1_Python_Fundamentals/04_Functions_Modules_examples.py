# 04_Functions_Modules_examples.py

# 1. Defining a simple function
def say_hello():
    print("Hello from a function!")

# calling the function
say_hello()

# 2. Function with parameters
def greet_user(username):
    print(f"Welcome, {username}!")

greet_user("Sriram")

# 3. Function with return value
def calculate_square(number):
    return number * number

result = calculate_square(5)
print("Square of 5 is:", result)

# 4. Using a built-in module
import math
import random

print("\n--- Using Modules ---")
print("Square root of 25 is:", math.sqrt(25))
print("Random number between 1 and 10:", random.randint(1, 10))
