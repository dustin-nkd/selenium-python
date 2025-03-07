# lambda.py

# 1. Basic Lambda Function
print("Example 1: Basic Lambda Function")

# A lambda function to add two numbers
add = lambda a, b: a + b

print("Sum:", add(5, 3))


# 2. Lambda with Single Argument
print("\nExample 2: Lambda with One Argument")

square = lambda x: x ** 2

print("Square of 4:", square(4))


# 3. Lambda with Multiple Arguments
print("\nExample 3: Lambda with Multiple Arguments")

max_num = lambda a, b: a if a > b else b

print("Maximum of (10, 20):", max_num(10, 20))


# 4. Lambda inside a Function
print("\nExample 4: Lambda Inside a Function")

def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
triple = multiplier(3)

print("Double of 5:", double(5))
print("Triple of 5:", triple(5))


# 5. Using Lambda with Built-in Functions (map, filter, sorted)
print("\nExample 5: Lambda with Map, Filter, and Sorted")

numbers = [1, 2, 3, 4, 5]

# Using map() to double each number
doubled_numbers = list(map(lambda x: x * 2, numbers))
print("Doubled numbers:", doubled_numbers)

# Using filter() to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# Using sorted() with lambda
students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
sorted_students = sorted(students, key=lambda student: student[1])
print("Sorted students by age:", sorted_students)