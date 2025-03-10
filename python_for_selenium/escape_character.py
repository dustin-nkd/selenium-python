# escape_character.py

# 1. Using a Newline Character (\n)
print("Example 1: Newline Character (\\n)")

text_with_newline = "Hello\nWorld!"
print(text_with_newline)


# 2. Using a Tab Character (\t)
print("\nExample 2: Tab Character (\\t)")

text_with_tab = "Python\tProgramming"
print(text_with_tab)


# 3. Using a Backslash (\\)
print("\nExample 3: Backslash (\\\\)")

text_with_backslash = "This is a backslash: \\"
print(text_with_backslash)


# 4. Using Single Quote (\')
print("\nExample 4: Single Quote (\\')")

text_with_single_quote = 'It\'s a sunny day!'
print(text_with_single_quote)


# 5. Using Double Quote (\")
print("\nExample 5: Double Quote (\\\")")

text_with_double_quote = "She said, \"Hello!\""
print(text_with_double_quote)


# 6. Using Carriage Return (\r)
print("\nExample 6: Carriage Return (\\r)")

text_with_carriage_return = "Hello\rWorld"
print(text_with_carriage_return)  # Overwrites "Hello" with "World"


# 7. Using Backspace (\b)
print("\nExample 7: Backspace (\\b)")

text_with_backspace = "Python\b3"
print(text_with_backspace)  # Removes the last character before '3'


# 8. Using Form Feed (\f)
print("\nExample 8: Form Feed (\\f)")

text_with_form_feed = "Hello\fWorld"
print(text_with_form_feed)


# 9. Using Unicode Characters (\u, \U, \N)
print("\nExample 9: Unicode Characters")

text_with_unicode = "Smiley Face: \u263A"
print(text_with_unicode)  # ☺ (Unicode smiley face)


# 10. Using Raw Strings (r"")
print("\nExample 10: Raw Strings (r\"\")")

raw_string = r"C:\Users\Name\Documents\new_file.txt"
print(raw_string)  # Displays the string as-is without escaping backslashes