# 06_String_Handling_examples.py

text = "  Python Programming is Fun!  "

# 1. Strip and Case conversion
print("Original:", f"'{text}'")
print("Stripped:", f"'{text.strip()}'")
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# 2. Slicing
word = "Python"
print("\nWord:", word)
print("First letter:", word[0])
print("Last letter:", word[-1])
print("Slice [0:2]:", word[0:2])

# 3. Replace and Split
new_text = text.replace("Fun", "Awesome")
print("\nReplaced:", new_text.strip())

words_list = text.strip().split(" ")
print("Split into list:", words_list)

# 4. Concatenation and Formatting
name = "Sriram"
f_string = f"Hello, {name}!"
print("\nF-String:", f_string)
