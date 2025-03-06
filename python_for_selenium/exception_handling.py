# exception_handling.py

# 1. Basic Try-Except Block
print("Example 1: Basic Try-Except")

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a valid number.")


# 2. Handling Multiple Exceptions
print("\nExample 2: Handling Multiple Exceptions")

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ValueError:
    print("Invalid input! Please enter numbers.")
except ZeroDivisionError:
    print("Error! Cannot divide by zero.")


# 3. Using Else with Try-Except
print("\nExample 3: Try-Except-Else")

try:
    num = int(input("Enter an even number: "))
    if num % 2 != 0:
        raise ValueError("This is not an even number!")
except ValueError as e:
    print("Exception:", e)
else:
    print("Good job! You entered an even number.")


# 4. Finally Block (Always Executes)
print("\nExample 4: Try-Except-Finally")

try:
    file = open("sample.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    print("Execution completed.")  # This will always execute


# 5. Custom Exception Handling
print("\nExample 5: Custom Exceptions")

class NegativeNumberError(Exception):
    """Custom exception for negative numbers"""
    pass

try:
    number = int(input("Enter a positive number: "))
    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
except NegativeNumberError as e:
    print("Exception:", e)
else:
    print("You entered:", number)