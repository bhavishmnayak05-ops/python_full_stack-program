# 05_Data_Structures_examples.py

# 1. List (Mutable, Ordered)
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits[1] = "blueberry"
print("List:", fruits)

# 2. Tuple (Immutable, Ordered)
coordinates = (10, 20)
print("Tuple:", coordinates)
# coordinates[0] = 15 # This would cause an error!

# 3. Set (Unordered, No duplicates)
unique_numbers = {1, 2, 3, 3, 2, 1}
print("Set:", unique_numbers) # Output will be {1, 2, 3}

# 4. Dictionary (Key:Value Pairs)
student = {
    "name": "Sriram",
    "course": "Python",
    "year": 2024
}
print("Dictionary:", student)
print("Student Name:", student["name"])
