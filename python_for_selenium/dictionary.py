# dictionary.py

# 1. Creating a dictionary
print("Example 1: Creating a dictionary")
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print("Person dictionary:", person)

# 2. Accessing dictionary values
print("\nExample 2: Accessing dictionary values")
print("Name:", person["name"])  # Access value by key
print("Age:", person["age"])

# 3. Using the get() method
print("\nExample 3: Using the get() method")
print("City:", person.get("city"))  # Access value using get() (returns None if key doesn't exist)

# 4. Modifying dictionary values
print("\nExample 4: Modifying dictionary values")
person["age"] = 26  # Modify the value of an existing key
print("Modified person dictionary:", person)

# 5. Adding a new key-value pair
print("\nExample 5: Adding a new key-value pair")
person["email"] = "alice@example.com"  # Add a new key-value pair
print("Person dictionary after adding a new key-value pair:", person)

# 6. Removing a key-value pair using del
print("\nExample 6: Removing a key-value pair using del")
del person["city"]  # Remove a key-value pair using del
print("Person dictionary after removing 'city':", person)

# 7. Removing a key-value pair using pop()
print("\nExample 7: Removing a key-value pair using pop()")
removed_value = person.pop("email")  # Remove and return the value of the key
print("Removed email:", removed_value)
print("Person dictionary after pop():", person)

# 8. Checking if a key exists
print("\nExample 8: Checking if a key exists")
if "name" in person:
    print("Name key exists in the dictionary.")
else:
    print("Name key does not exist in the dictionary.")

# 9. Iterating through a dictionary
print("\nExample 9: Iterating through a dictionary")
for key, value in person.items():  # Iterate through keys and values
    print(f"{key}: {value}")

# 10. Dictionary keys() method
print("\nExample 10: Dictionary keys() method")
keys = person.keys()  # Get all the keys in the dictionary
print("Keys in the person dictionary:", keys)

# 11. Dictionary values() method
print("\nExample 11: Dictionary values() method")
values = person.values()  # Get all the values in the dictionary
print("Values in the person dictionary:", values)

# 12. Dictionary items() method
print("\nExample 12: Dictionary items() method")
items = person.items()  # Get all the key-value pairs as tuples
print("Key-value pairs in the person dictionary:", items)

# 13. Dictionary comprehension
print("\nExample 13: Dictionary comprehension")
squared_numbers_dict = {x: x**2 for x in range(1, 6)}  # Create a dictionary of squares of numbers
print("Squared numbers dictionary:", squared_numbers_dict)

# 14. Nested dictionaries
print("\nExample 14: Nested dictionaries")
people = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}
print("Nested dictionary:", people)
print("Accessing nested dictionary:", people["person1"]["name"])  # Access nested dictionary value