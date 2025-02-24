# classes_and_objects.py

# 1. Defining a simple class
print("Example 1: Defining a simple class")

class Person:
    # Constructor method (__init__) to initialize object attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display information
    def introduce(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old."

# Creating an object of the Person class
person1 = Person("Alice", 25)
print(person1.introduce())


# 2. Creating multiple objects
print("\nExample 2: Creating multiple objects")
person2 = Person("Bob", 30)
person3 = Person("Charlie", 22)

print(person2.introduce())
print(person3.introduce())


# 3. Modifying object attributes
print("\nExample 3: Modifying object attributes")
person1.age = 26  # Changing age attribute
print(f"Updated age of {person1.name}: {person1.age}")


# 4. Adding a new attribute dynamically
print("\nExample 4: Adding a new attribute dynamically")
person1.city = "New York"  # Adding a new attribute to person1 only
print(f"{person1.name} lives in {person1.city}.")


# 5. Class with a default attribute
print("\nExample 5: Class with a default attribute")

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.running = False  # Default attribute

    def start(self):
        self.running = True
        return f"{self.brand} {self.model} is now running."

car1 = Car("Toyota", "Corolla", 2022)
print(f"Car Status: {car1.running}")  # Default is False
print(car1.start())  # Calling the start method
print(f"Car Status after starting: {car1.running}")


# 6. Using class variables (shared among all objects)
print("\nExample 6: Using class variables")

class Employee:
    company = "TechCorp"  # Class variable (shared by all instances)

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        return f"{self.name} works at {Employee.company} and earns ${self.salary}."

emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

print(emp1.show_info())
print(emp2.show_info())

# Changing the class variable affects all objects
Employee.company = "NewTech"
print(emp1.show_info())
print(emp2.show_info())


# 7. Private attributes and methods
print("\nExample 7: Private attributes and methods")

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount
        return f"${amount} deposited. New balance: ${self.__balance}"

    def get_balance(self):
        return f"Current balance: ${self.__balance}"

# Creating an object
account1 = BankAccount("Alice", 1000)
print(account1.deposit(500))
print(account1.get_balance())

# Uncommenting the next line will raise an AttributeError
# print(account1.__balance)  # Cannot access private attribute directly


# 8. Class methods and static methods
print("\nExample 8: Class methods and static methods")

class MathUtils:
    pi = 3.14159

    @classmethod
    def circle_area(cls, radius):
        return cls.pi * (radius ** 2)

    @staticmethod
    def add(x, y):
        return x + y

print(f"Circle area with radius 5: {MathUtils.circle_area(5)}")
print(f"Addition of 3 and 7: {MathUtils.add(3, 7)}")