# kwargs.py

# 1. Basic **kwargs Usage
print("Example 1: Using **kwargs in a Function")

def print_info(**kwargs):
    """Prints all key-value pairs provided as keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")


# 2. **kwargs with Regular Parameters
print("\nExample 2: **kwargs with Regular Parameters")

def student_info(course, **kwargs):
    """Prints course name and additional student information."""
    print(f"Course: {course}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_info("Python Basics", name="Bob", age=22, city="London")


# 3. Iterating Over **kwargs
print("\nExample 3: Iterating Over **kwargs")

def print_details(**kwargs):
    """Print each key-value pair."""
    for key in kwargs:
        print(f"{key} -> {kwargs[key]}")

print_details(first="John", last="Doe", job="Developer")


# 4. Mixing *args and **kwargs
print("\nExample 4: Mixing *args and **kwargs")

def display_info(*args, **kwargs):
    """Displays both positional and keyword arguments."""
    print("Positional arguments:")
    for arg in args:
        print(arg)

    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info("Apple", "Banana", name="Charlie", age=30)


# 5. Unpacking Dictionary into **kwargs
print("\nExample 5: Unpacking Dictionary into **kwargs")

def show_info(name, age, city):
    """Displays person information."""
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")

person = {"name": "Eve", "age": 28, "city": "Paris"}
show_info(**person)  # Unpacking dictionary