# while_loop.py

# 1. Basic while loop
print("Example 1: Basic while loop")
counter = 1
while counter <= 5:  # The loop will run as long as counter is less than or equal to 5
    print("Counter is:", counter)
    counter += 1  # Increment counter by 1 each time

# 2. While loop with a condition
print("\nExample 2: While loop with a condition")
num = 10
while num > 0:  # Loop continues while num is greater than 0
    print(f"Number is: {num}")
    num -= 2  # Decrease num by 2 each time

# 3. Infinite while loop (with a break condition)
print("\nExample 3: Infinite while loop with break")
while True:  # This creates an infinite loop
    user_input = input("Enter 'quit' to stop the loop: ")
    if user_input == "quit":
        print("Loop stopped.")
        break  # Exit the loop when 'quit' is entered

# 4. While loop with a continue statement
print("\nExample 4: Using continue in while loop")
x = 0
while x < 10:
    x += 1
    if x == 5:
        continue  # Skip the rest of the loop when x is 5
    print(f"x is: {x}")

# 5. Nested while loops
print("\nExample 5: Nested while loops")
outer_counter = 1
while outer_counter <= 3:  # Outer loop
    inner_counter = 1
    while inner_counter <= 2:  # Inner loop
        print(f"Outer: {outer_counter}, Inner: {inner_counter}")
        inner_counter += 1
    outer_counter += 1

# 6. Using while loop to sum numbers
print("\nExample 6: Using while loop to sum numbers")
total = 0
num = 1
while num <= 5:
    total += num  # Add num to total
    num += 1  # Increment num by 1
print(f"The total sum is: {total}")