# for_loop_with_range.py

# 1. Using range() in a basic for loop
# range(start, stop, step)
print("Example 1: Basic for loop with range()")
for i in range(5):  # Loop from 0 to 4 (5 not included)
    print(i)

# 2. Using range with start and stop
print("\nExample 2: for loop with start and stop")
for i in range(2, 8):  # Loop from 2 to 7 (8 not included)
    print(i)

# 3. Using range with start, stop, and step
print("\nExample 3: for loop with start, stop, and step")
for i in range(1, 10, 2):  # Loop from 1 to 9, with a step of 2
    print(i)

# 4. Reverse loop
print("\nExample 4: Reverse for loop")
for i in range(10, 0, -1):  # Loop from 10 down to 1
    print(i)

# 5. Using range() with a list
print("\nExample 5: Using range() with list")
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):  # Loop through the indices of the list fruits
    print(f"Index {i}: {fruits[i]}")

# 6. Using range() to print even numbers
print("\nExample 6: Using range() to print even numbers")
for i in range(0, 20, 2):  # Loop from 0 to 19, with a step of 2
    print(i)

# 7. Using range() combined with a condition
print("\nExample 7: Using range() with a condition")
for i in range(1, 11):
    if i % 2 == 0:  # Check if the number is even
        print(f"{i} is even")
    else:
        print(f"{i} is odd")