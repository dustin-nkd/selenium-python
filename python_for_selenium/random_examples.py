# random_examples.py

import random  # Importing the random module

# 1. Generate a Random Integer
print("Example 1: Generate a Random Integer")

random_number = random.randint(1, 100)  # Random number between 1 and 100
print("Random number:", random_number)


# 2. Generate a Random Float
print("\nExample 2: Generate a Random Float")

random_float = random.uniform(1.5, 5.5)  # Random float between 1.5 and 5.5
print("Random float:", random_float)


# 3. Choose a Random Element from a List
print("\nExample 3: Choose a Random Element from a List")

fruits = ["Apple", "Banana", "Cherry", "Mango", "Grapes"]
random_fruit = random.choice(fruits)
print("Random fruit:", random_fruit)


# 4. Shuffle a List Randomly
print("\nExample 4: Shuffle a List")

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)  # Shuffling the list
print("Shuffled list:", numbers)


# 5. Generate a Random Sample (Multiple Unique Elements)
print("\nExample 5: Generate a Random Sample")

sample_numbers = random.sample(range(1, 50), 5)  # 5 unique random numbers from 1 to 50
print("Random sample:", sample_numbers)


# 6. Generate a Random Boolean
print("\nExample 6: Generate a Random Boolean")

random_boolean = random.choice([True, False])
print("Random boolean:", random_boolean)


# 7. Generate a Random String from Characters
print("\nExample 7: Generate a Random String")

import string  # Importing string module for characters
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
print("Random string:", random_string)