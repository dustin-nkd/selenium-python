# print_statements.py - Guide to Print Statements in Python

# 1. Basic Print Statement
print("Hello, World!")

# 2. Printing Multiple Values
name = "Alice"
age = 25
print("Name:", name, "Age:", age)

# 3. Using f-strings (Python 3.6+)
print(f"My name is {name} and I am {age} years old.")

# 4. Using .format() Method
print("My name is {} and I am {} years old.".format(name, age))

# 5. Printing with Separator
a, b, c = 1, 2, 3
print(a, b, c, sep=" - ")

# 6. Printing with End Parameter
print("Hello", end=" ")
print("World!")  # This will print on the same line

# 7. Printing Special Characters
print("Hello\nWorld")  # Newline character
print("Tab\tSeparated")  # Tab character

# 8. Printing a Raw String
print(r"C:\Users\Alice\Documents")  # Prevents escape sequences

# 9. Printing Using Unicode Characters
print("Smile Emoji:", "\U0001F600")