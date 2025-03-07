# args.py

# 1. Basic *args Usage
print("Example 1: Using *args in a Function")

def add_numbers(*args):
    """Function that takes multiple numbers and returns their sum."""
    return sum(args)

print("Sum of 1, 2, 3:", add_numbers(1, 2, 3))
print("Sum of 5, 10, 15, 20:", add_numbers(5, 10, 15, 20))


# 2. *args with Other Parameters
print("\nExample 2: *args with Regular Parameters")

def greet(message, *names):
    """Function that prints a greeting message to multiple people."""
    for name in names:
        print(f"{message}, {name}!")

greet("Hello", "Alice", "Bob", "Charlie")
greet("Good morning", "David")


# 3. Using *args in a Loop
print("\nExample 3: Iterating Over *args")

def print_details(*args):
    """Prints all details provided."""
    for detail in args:
        print(detail)

print_details("John", 25, "Developer", "New York")


# 4. Mixing *args with Keyword Arguments
print("\nExample 4: Mixing *args with Keyword Arguments")

def student_info(course, *students):
    """Prints student names enrolled in a course."""
    print(f"Course: {course}")
    print("Enrolled Students:")
    for student in students:
        print("-", student)

student_info("Python Basics", "Alice", "Bob", "Charlie")


# 5. Unpacking a List or Tuple as *args
print("\nExample 5: Unpacking a List/Tuple into *args")

numbers = [2, 4, 6, 8]
print("Sum of numbers:", add_numbers(*numbers))  # Unpacking list

values = (10, 20, 30)
print("Sum of values:", add_numbers(*values))  # Unpacking tuple