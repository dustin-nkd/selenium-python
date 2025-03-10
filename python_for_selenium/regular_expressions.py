# regular_expressions.py

import re  # Importing the regular expressions module

# 1. Check if a string contains a pattern using re.search()
print("Example 1: Using re.search()")

text = "Hello, my email is example@gmail.com"
pattern = r"\w+@\w+\.\w+"  # Regex pattern for an email

match = re.search(pattern, text)
if match:
    print("Found email:", match.group())  # Extracts the email


# 2. Find all occurrences of a pattern using re.findall()
print("\nExample 2: Using re.findall()")

text = "The numbers are 42, 100, and 35."
pattern = r"\d+"  # Regex pattern for numbers

matches = re.findall(pattern, text)
print("Numbers found:", matches)


# 3. Replace text using re.sub()
print("\nExample 3: Using re.sub()")

text = "I love Python! Python is fun."
pattern = r"Python"

new_text = re.sub(pattern, "JavaScript", text)  # Replacing "Python" with "JavaScript"
print("Modified text:", new_text)


# 4. Splitting a string using re.split()
print("\nExample 4: Using re.split()")

text = "apple, banana; cherry|grape"
pattern = r"[,;|]"  # Splitting on multiple delimiters

split_text = re.split(pattern, text)
print("Split text:", split_text)


# 5. Using re.match() to check if a string starts with a pattern
print("\nExample 5: Using re.match()")

text = "Python is awesome!"
pattern = r"Python"

if re.match(pattern, text):
    print("The string starts with 'Python'.")


# 6. Using re.compile() for repeated pattern matching
print("\nExample 6: Using re.compile()")

pattern = re.compile(r"\d{3}-\d{2}-\d{4}")  # Pattern for a Social Security Number (SSN)

text1 = "My SSN is 123-45-6789."
text2 = "Invalid number: 12-3456-789."

print("Valid SSN found:", pattern.search(text1))
print("Valid SSN found in second text:", pattern.search(text2))


# 7. Using Groups in Regex
print("\nExample 7: Using Groups in Regex")

text = "Phone number: (123) 456-7890"
pattern = r"\((\d{3})\) (\d{3})-(\d{4})"  # Capturing area code and numbers

match = re.search(pattern, text)
if match:
    print("Full Match:", match.group(0))
    print("Area Code:", match.group(1))
    print("First 3 Digits:", match.group(2))
    print("Last 4 Digits:", match.group(3))