# string.py

# 1. Creating a string
print("Example 1: Creating a string")
message = "Hello, Python!"
print("Message:", message)

# 2. Accessing characters in a string
print("\nExample 2: Accessing characters in a string")
print("First character:", message[0])  # First character
print("Last character:", message[-1])  # Last character

# 3. String slicing
print("\nExample 3: String slicing")
print("First 5 characters:", message[:5])  # First 5 characters
print("Last 6 characters:", message[-6:])  # Last 6 characters
print("Characters from index 7 to 12:", message[7:12])  # Characters from index 7 to 12

# 4. String length
print("\nExample 4: String length")
print("Length of the message:", len(message))

# 5. Changing case
print("\nExample 5: Changing case")
print("Uppercase:", message.upper())  # Convert to uppercase
print("Lowercase:", message.lower())  # Convert to lowercase

# 6. Removing whitespace
print("\nExample 6: Removing whitespace")
text_with_spaces = "   Hello, Python!   "
print("Original text:", f"'{text_with_spaces}'")
print("Stripped text:", f"'{text_with_spaces.strip()}'")  # Remove leading and trailing spaces

# 7. String concatenation
print("\nExample 7: String concatenation")
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"
print("Concatenated string:", full_greeting)

# 8. Repeating strings
print("\nExample 8: Repeating strings")
repeat_str = "Python! " * 3
print("Repeated string:", repeat_str)

# 9. Checking if a substring exists
print("\nExample 9: Checking if a substring exists")
if "Python" in message:
    print("'Python' is found in the message")
else:
    print("'Python' is not found in the message")

# 10. Replacing text in a string
print("\nExample 10: Replacing text in a string")
new_message = message.replace("Python", "World")
print("Updated message:", new_message)

# 11. Splitting a string
print("\nExample 11: Splitting a string")
sentence = "apple,banana,orange"
fruits_list = sentence.split(",")  # Split string by commas
print("Split list:", fruits_list)

# 12. Joining a list of strings
print("\nExample 12: Joining a list of strings")
joined_string = " - ".join(fruits_list)
print("Joined string:", joined_string)

# 13. Formatting strings using f-strings
print("\nExample 13: Formatting strings using f-strings")
age = 25
formatted_string = f"My name is {name} and I am {age} years old."
print("Formatted string:", formatted_string)

# 14. Finding a substring
print("\nExample 14: Finding a substring")
position = message.find("Python")  # Returns index of first occurrence
print("Position of 'Python':", position)

# 15. Counting occurrences of a substring
print("\nExample 15: Counting occurrences of a substring")
text = "banana banana apple banana"
count = text.count("banana")
print("Occurrences of 'banana':", count)

# 16. Reversing a string
print("\nExample 16: Reversing a string")
reversed_string = message[::-1]  # Reverse the string using slicing
print("Reversed message:", reversed_string)