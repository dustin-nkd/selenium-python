# tuple.py

# 1. Creating a tuple
print("Example 1: Creating a tuple")
fruits_tuple = ("apple", "banana", "cherry")
print("Fruits tuple:", fruits_tuple)

# 2. Accessing tuple elements
print("\nExample 2: Accessing tuple elements")
print("First fruit:", fruits_tuple[0])  # Access the first element
print("Last fruit:", fruits_tuple[-1])  # Access the last element

# 3. Slicing a tuple
print("\nExample 3: Slicing a tuple")
sub_tuple = fruits_tuple[1:3]  # Get a subtuple from index 1 to 2
print("Subtuple from index 1 to 2:", sub_tuple)

# 4. Tuple with one element (singleton tuple)
print("\nExample 4: Tuple with one element (singleton tuple)")
single_element_tuple = ("apple",)  # Adding a comma makes it a tuple
print("Singleton tuple:", single_element_tuple)

# 5. Concatenating tuples
print("\nExample 5: Concatenating tuples")
vegetables_tuple = ("carrot", "broccoli")
combined_tuple = fruits_tuple + vegetables_tuple  # Concatenate two tuples
print("Combined tuple:", combined_tuple)

# 6. Repeating a tuple
print("\nExample 6: Repeating a tuple")
repeated_tuple = fruits_tuple * 2  # Repeat the tuple twice
print("Repeated tuple:", repeated_tuple)

# 7. Checking if an item exists in a tuple
print("\nExample 7: Checking if an item exists in a tuple")
if "banana" in fruits_tuple:
    print("Banana is in the fruits tuple.")
else:
    print("Banana is not in the fruits tuple.")

# 8. Finding the index of an element
print("\nExample 8: Finding the index of an element")
index_of_cherry = fruits_tuple.index("cherry")  # Find the index of "cherry"
print("Index of cherry:", index_of_cherry)

# 9. Counting occurrences of an element
print("\nExample 9: Counting occurrences of an element")
count_of_apple = fruits_tuple.count("apple")  # Count how many times "apple" appears
print("Number of apples in tuple:", count_of_apple)

# 10. Tuple unpacking
print("\nExample 10: Tuple unpacking")
a, b, c = fruits_tuple  # Unpack the tuple into individual variables
print("Unpacked elements:", a, b, c)

# 11. Nested tuples
print("\nExample 11: Nested tuples")
nested_tuple = ("apple", ("orange", "pear"), "banana")
print("Nested tuple:", nested_tuple)
print("Accessing nested tuple element:", nested_tuple[1][0])  # Access the first element of the nested tuple

# 12. Iterating through a tuple
print("\nExample 12: Iterating through a tuple")
for fruit in fruits_tuple:
    print("Fruit:", fruit)

# 13. Tuple as a key in a dictionary
print("\nExample 13: Using a tuple as a key in a dictionary")
tuple_key = ("name", "age")
person = {tuple_key: "Alice"}
print("Dictionary with tuple as key:", person)