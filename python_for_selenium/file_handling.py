# file_handling.py

# 1. Writing to a file
print("Example 1: Writing to a file")
with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("Python makes file handling easy!\n")
print("Data written to 'example.txt'.")

# 2. Reading from a file
print("\nExample 2: Reading from a file")
with open("example.txt", "r") as file:
    content = file.read()
print("File content:\n", content)

# 3. Appending to a file
print("\nExample 3: Appending to a file")
with open("example.txt", "a") as file:
    file.write("This line was added later.\n")
print("New data appended to 'example.txt'.")

# 4. Reading file line by line
print("\nExample 4: Reading file line by line")
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # Remove extra newline characters

# 5. Using readlines() to get a list of lines
print("\nExample 5: Using readlines() to get a list of lines")
with open("example.txt", "r") as file:
    lines = file.readlines()
print("Lines as a list:", lines)

# 6. Writing a list to a file
print("\nExample 6: Writing a list to a file")
lines_to_write = ["Apple\n", "Banana\n", "Cherry\n"]
with open("fruits.txt", "w") as file:
    file.writelines(lines_to_write)
print("List written to 'fruits.txt'.")

# 7. Reading a file safely using try-except
print("\nExample 7: Handling file errors with try-except")
try:
    with open("non_existent.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found. Please check the filename.")

# 8. Checking if a file exists before reading
print("\nExample 8: Checking if a file exists")
import os

filename = "example.txt"
if os.path.exists(filename):
    with open(filename, "r") as file:
        print(f"Reading '{filename}':\n{file.read()}")
else:
    print(f"File '{filename}' does not exist.")

# 9. Deleting a file
print("\nExample 9: Deleting a file")
file_to_delete = "fruits.txt"
if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print(f"'{file_to_delete}' has been deleted.")
else:
    print(f"'{file_to_delete}' does not exist, so it cannot be deleted.")