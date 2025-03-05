# private_variable_private_method.py

# 1. Private Variables (Using Double Underscore `__`)
print("Example 1: Private Variables")

class Person:
    def __init__(self, name, age):
        self.name = name  # Public variable
        self.__age = age  # Private variable (name mangling applied)

    def get_age(self):  # Public method to access the private variable
        return self.__age

# Creating an object
person1 = Person("Alice", 30)

print(f"Name: {person1.name}")  # Accessible
# print(person1.__age)  # This will raise an AttributeError
print(f"Age (using method): {person1.get_age()}")  # Accessed using a method


# 2. Private Methods (Using Double Underscore `__`)
print("\nExample 2: Private Methods")

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private variable

    def __apply_interest(self):  # Private method
        self.__balance *= 1.05  # Adds 5% interest

    def get_balance(self):
        self.__apply_interest()  # Calling private method inside a public method
        return self.__balance

# Creating an object
account1 = BankAccount("Bob", 1000)

# print(account1.__apply_interest())  # This will raise an AttributeError
print(f"Balance after interest: {account1.get_balance()}")  # Accessed indirectly


# 3. Accessing Private Variables using Name Mangling
print("\nExample 3: Accessing Private Variables with Name Mangling")

class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.__price = price  # Private variable

    def get_price(self):
        return self.__price

# Creating an object
car1 = Car("Tesla", 50000)

# print(car1.__price)  # This will raise an AttributeError
print(f"Car price (using method): {car1.get_price()}")

# Accessing private variable using name mangling
print(f"Car price (using name mangling): {car1._Car__price}")  # Not recommended


# 4. Private Methods using Name Mangling
print("\nExample 4: Calling Private Methods with Name Mangling")

class Robot:
    def __init__(self, model):
        self.model = model

    def __secret_code(self):
        return "42-XYZ"

    def reveal_code(self):
        return self.__secret_code()  # Proper way to access private methods

# Creating an object
robot1 = Robot("RX-1000")

# print(robot1.__secret_code())  # This will raise an AttributeError
print(f"Secret code (using method): {robot1.reveal_code()}")

# Calling private method using name mangling
print(f"Secret code (using name mangling): {robot1._Robot__secret_code()}")  # Not recommended