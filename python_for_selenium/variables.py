# variables.py - Guide to Variables in Python

# 1. Declaring Variables
name = "Alice"  # String variable
age = 25        # Integer variable
height = 1.68   # Float variable
is_student = True  # Boolean variable (True/False)

# 2. Printing Variable Values
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# 3. Reassigning Variables
name = "Bob"
age = age + 1  # Incrementing age by 1

print("After updating:")
print("New Name:", name)
print("New Age:", age)

# 4. Declaring Multiple Variables at Once
a, b, c = 10, 20, 30
print("Values of a, b, c:", a, b, c)

# 5. Variable Naming Conventions
# - Can contain letters, numbers, and underscores (_)
# - Cannot start with a number
# - Case-sensitive
my_variable = "Hello"
MyVariable = "World"

print(my_variable, MyVariable)

# 6. Dynamic Typing in Python
x = 100   # x is an integer
print("Type of x:", type(x))
x = "Python"  # x is now a string
print("Type of x after change:", type(x))