# 08_File_Handling_examples.py

# 1. Writing to a file
print("Writing to sample.txt...")
with open("sample.txt", "w") as file:
    file.write("Line 1: Learning Python File Handling.\n")
    file.write("Line 2: It is very simple!\n")

# 2. Reading the whole file
print("\nReading sample.txt:")
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# 3. Appending to a file
print("Appending to sample.txt...")
with open("sample.txt", "a") as file:
    file.write("Line 3: This line was appended later.\n")

# 4. Reading line by line
print("\nReading line by line:")
with open("sample.txt", "r") as file:
    for line in file:
        print("Data:", line.strip())
