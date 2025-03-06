# import_module.py

# Import the entire module
import my_module

print(my_module.greet("Alice"))
print("Sum:", my_module.add(5, 7))
print("Value of PI:", my_module.PI)

# Import specific functions
from my_module import greet, add

print(greet("Bob"))  # No need to use module name now
print("Sum:", add(10, 20))

# Import with an alias
import my_module as mm

print(mm.greet("Charlie"))