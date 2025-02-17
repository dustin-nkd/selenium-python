# storing_text.py

# 1. Storing a single line of text in a variable
print("Example 1: Storing a single line of text in a variable")
text = "Hello, this is a simple text stored in a variable."
print("Stored text:", text)

# 2. Storing multiple lines of text in a variable (using multi-line string)
print("\nExample 2: Storing multiple lines of text in a variable")
multi_line_text = """This is the first line of text.
This is the second line.
This is the third line of text."""
print("Stored text:\n", multi_line_text)

# 3. Storing text with variables inside (using f-string)
print("\nExample 3: Storing text with variables inside (f-string)")
name = "Alice"
age = 25
greeting = f"My name is {name} and I am {age} years old."
print("Stored text:", greeting)

# 4. Modifying the stored text by concatenating
print("\nExample 4: Modifying the stored text by concatenating")
text_part1 = "Hello"
text_part2 = "World"
combined_text = text_part1 + ", " + text_part2 + "!"  # Concatenating two strings
print("Combined text:", combined_text)

# 5. Using variables to create dynamic text
print("\nExample 5: Using variables to create dynamic text")
city = "Paris"
country = "France"
location_description = f"{city} is located in {country}."
print("Dynamic text:", location_description)