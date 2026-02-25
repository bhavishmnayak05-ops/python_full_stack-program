# 03_Operators_Control_examples.py

# 1. Operators
x = 10
y = 3

print("--- Arithmetic Operators ---")
print("x + y =", x + y)
print("x / y =", x / y)
print("x // y =", x // y)  # Floor division (removes decimal)
print("x % y =", x % y)    # Modulus (remainder)
print("x ** y =", x ** y)  # Power (10 to the power 3)

# 2. Control Statements (if-else)
print("\n--- Control Statements ---")
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")

# 3. Loops
print("\n--- For Loop (range) ---")
for i in range(1, 4):
    print("Loop iteration:", i)

print("\n--- While Loop ---")
count = 1
while count <= 3:
    print("Count is:", count)
    count += 1
