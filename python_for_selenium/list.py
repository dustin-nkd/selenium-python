# list.py

# 1. Creating a list
print("Example 1: Creating a list")
fruits = ["apple", "banana", "cherry"]
print("Fruits list:", fruits)

# 2. Accessing list elements
print("\nExample 2: Accessing list elements")
print("First fruit:", fruits[0])  # Access the first element
print("Last fruit:", fruits[-1])  # Access the last element

# 3. Modifying list elements
print("\nExample 3: Modifying list elements")
fruits[1] = "blueberry"  # Change the second element
print("Modified fruits list:", fruits)

# 4. Adding elements to a list
print("\nExample 4: Adding elements to a list")
fruits.append("orange")  # Add an element to the end of the list
print("Fruits list after adding an element:", fruits)

# 5. Inserting elements at a specific position
print("\nExample 5: Inserting elements at a specific position")
fruits.insert(1, "grape")  # Insert "grape" at index 1
print("Fruits list after insertion:", fruits)

# 6. Removing elements from a list
print("\nExample 6: Removing elements from a list")
fruits.remove("banana")  # Remove the element "banana"
print("Fruits list after removal:", fruits)

# 7. Popping an element from the list
print("\nExample 7: Popping an element from the list")
popped_fruit = fruits.pop()  # Remove and return the last element
print("Popped fruit:", popped_fruit)
print("Fruits list after popping:", fruits)

# 8. List slicing
print("\nExample 8: List slicing")
sublist = fruits[1:3]  # Get a sublist from index 1 to 2
print("Sublist from index 1 to 2:", sublist)

# 9. Iterating through a list
print("\nExample 9: Iterating through a list")
for fruit in fruits:
    print("Fruit:", fruit)

# 10. List comprehension
print("\nExample 10: List comprehension")
squared_numbers = [x**2 for x in range(1, 6)]  # Create a list of squares of numbers from 1 to 5
print("Squared numbers:", squared_numbers)

# 11. Checking if an item exists in a list
print("\nExample 11: Checking if an item exists in a list")
if "apple" in fruits:
    print("Apple is in the fruits list.")
else:
    print("Apple is not in the fruits list.")

# 12. Finding the index of an element
print("\nExample 12: Finding the index of an element")
index_of_cherry = fruits.index("cherry")  # Find the index of "cherry"
print("Index of cherry:", index_of_cherry)

# 13. Sorting a list
print("\nExample 13: Sorting a list")
fruits.sort()  # Sort the list in ascending order
print("Sorted fruits list:", fruits)

# 14. Reversing a list
print("\nExample 14: Reversing a list")
fruits.reverse()  # Reverse the list
print("Reversed fruits list:", fruits)