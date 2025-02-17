# set.py

# 1. Creating a set
print("Example 1: Creating a set")
fruits_set = {"apple", "banana", "cherry"}
print("Fruits set:", fruits_set)

# 2. Adding elements to a set
print("\nExample 2: Adding elements to a set")
fruits_set.add("orange")  # Add a single element
print("Fruits set after adding an element:", fruits_set)

# 3. Adding multiple elements using update
print("\nExample 3: Adding multiple elements using update()")
fruits_set.update(["grape", "mango"])  # Add multiple elements at once
print("Fruits set after adding multiple elements:", fruits_set)

# 4. Removing elements from a set
print("\nExample 4: Removing elements from a set")
fruits_set.remove("banana")  # Remove a specific element
print("Fruits set after removing 'banana':", fruits_set)

# 5. Removing an element using discard (no error if element is not found)
print("\nExample 5: Removing an element using discard()")
fruits_set.discard("pear")  # Discard an element (no error if element is not found)
print("Fruits set after discard (no 'pear' present):", fruits_set)

# 6. Popping an element from a set
print("\nExample 6: Popping an element from a set")
popped_fruit = fruits_set.pop()  # Remove and return an arbitrary element
print("Popped fruit:", popped_fruit)
print("Fruits set after popping an element:", fruits_set)

# 7. Checking if an item exists in a set
print("\nExample 7: Checking if an item exists in a set")
if "cherry" in fruits_set:
    print("Cherry is in the fruits set.")
else:
    print("Cherry is not in the fruits set.")

# 8. Set operations: Union
print("\nExample 8: Set union")
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)  # Union of two sets
print("Union of set1 and set2:", union_set)

# 9. Set operations: Intersection
print("\nExample 9: Set intersection")
intersection_set = set1.intersection(set2)  # Intersection of two sets
print("Intersection of set1 and set2:", intersection_set)

# 10. Set operations: Difference
print("\nExample 10: Set difference")
difference_set = set1.difference(set2)  # Difference of set1 from set2
print("Difference of set1 and set2:", difference_set)

# 11. Set operations: Symmetric difference
print("\nExample 11: Set symmetric difference")
symmetric_difference_set = set1.symmetric_difference(set2)  # Symmetric difference
print("Symmetric difference between set1 and set2:", symmetric_difference_set)

# 12. Set length
print("\nExample 12: Set length")
set_length = len(fruits_set)  # Get the length of the set
print("The length of the fruits set is:", set_length)

# 13. Iterating through a set
print("\nExample 13: Iterating through a set")
for fruit in fruits_set:
    print("Fruit:", fruit)

# 14. Set comprehension
print("\nExample 14: Set comprehension")
squared_numbers_set = {x**2 for x in range(1, 6)}  # Create a set of squares of numbers from 1 to 5
print("Set of squared numbers:", squared_numbers_set)