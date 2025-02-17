# function.py

# 1. Defining a basic function
print("Example 1: Defining a basic function")
def greet():
    print("Hello, welcome to Python programming!")

# Calling the function
greet()

# 2. Function with parameters
print("\nExample 2: Function with parameters")
def greet_person(name):
    print(f"Hello, {name}! Welcome to Python programming!")

# Calling the function with an argument
greet_person("Alice")
greet_person("Bob")

# 3. Function with a return value
print("\nExample 3: Function with a return value")
def add_numbers(a, b):
    return a + b

# Calling the function and printing the result
result = add_numbers(5, 3)
print("The result of adding 5 and 3 is:", result)

# 4. Function with default parameter values
print("\nExample 4: Function with default parameter values")
def greet_person_default(name="Guest"):
    print(f"Hello, {name}! Welcome to Python programming!")

# Calling the function with and without passing a parameter
greet_person_default("Alice")
greet_person_default()

# 5. Function with multiple parameters and return
print("\nExample 5: Function with multiple parameters and return")
def multiply_numbers(a, b, c):
    return a * b * c

# Calling the function and printing the result
result = multiply_numbers(2, 3, 4)
print("The result of multiplying 2, 3, and 4 is:", result)

# 6. Function with keyword arguments
print("\nExample 6: Function with keyword arguments")
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

# Calling the function with keyword arguments
describe_person(age=30, name="John", city="New York")

# 7. Function with arbitrary arguments (*args)
print("\nExample 7: Function with arbitrary arguments (*args)")
def print_numbers(*args):
    for number in args:
        print(number)

# Calling the function with multiple arguments
print_numbers(1, 2, 3, 4, 5)

# 8. Function with arbitrary keyword arguments (**kwargs)
print("\nExample 8: Function with arbitrary keyword arguments (**kwargs)")
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with multiple keyword arguments
print_info(name="Alice", age=25, city="Paris")