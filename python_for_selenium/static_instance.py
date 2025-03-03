# static_variables_static_methods_instance_variables_instance_methods.py

# 1. Instance Variables and Instance Methods
print("Example 1: Instance Variables and Instance Methods")

class Person:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

    def introduce(self):  # Instance method
        return f"Hi, my name is {self.name} and I am {self.age} years old."

# Creating objects with different instance variables
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.introduce())
print(person2.introduce())


# 2. Static Variables (Class Variables)
print("\nExample 2: Static Variables (Class Variables)")

class Employee:
    company = "TechCorp"  # Static variable (shared by all instances)

    def __init__(self, name, salary):
        self.name = name  # Instance variable
        self.salary = salary  # Instance variable

    def show_info(self):
        return f"{self.name} works at {Employee.company} and earns ${self.salary}."

# Creating objects
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

print(emp1.show_info())
print(emp2.show_info())

# Modifying the class variable
Employee.company = "NewTech"

# All instances reflect the change in the class variable
print(emp1.show_info())
print(emp2.show_info())


# 3. Instance Methods (Can Access Both Instance and Static Variables)
print("\nExample 3: Instance Methods Accessing Instance and Static Variables")

class Car:
    brand = "Toyota"  # Static variable

    def __init__(self, model, year):
        self.model = model  # Instance variable
        self.year = year    # Instance variable

    def display_info(self):  # Instance method
        return f"{Car.brand} {self.model}, Year: {self.year}"

# Creating objects
car1 = Car("Corolla", 2022)
car2 = Car("Camry", 2023)

print(car1.display_info())
print(car2.display_info())


# 4. Static Methods (Independent Methods That Don't Use `self`)
print("\nExample 4: Static Methods (Do Not Use `self`)")

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# Calling static methods without creating an instance
print(f"Addition: {MathUtils.add(5, 3)}")
print(f"Multiplication: {MathUtils.multiply(4, 6)}")


# 5. Difference Between Static and Instance Methods
print("\nExample 5: Comparing Static Methods and Instance Methods")

class Animal:
    kingdom = "Animalia"  # Static variable

    def __init__(self, name):
        self.name = name  # Instance variable

    def get_name(self):  # Instance method (uses `self`)
        return f"Animal name: {self.name}"

    @staticmethod
    def get_kingdom():  # Static method (does not use `self`)
        return f"Kingdom: {Animal.kingdom}"

# Creating an object
animal1 = Animal("Lion")

# Calling instance method (requires an object)
print(animal1.get_name())

# Calling static method (does not require an object)
print(Animal.get_kingdom())


# 6. Class Methods (Alternative to Static Methods, Using `cls`)
print("\nExample 6: Class Methods Using `cls`")

class Product:
    category = "Electronics"  # Static variable

    def __init__(self, name, price):
        self.name = name  # Instance variable
        self.price = price  # Instance variable

    @classmethod
    def set_category(cls, new_category):  # Class method (modifies static variable)
        cls.category = new_category

    @classmethod
    def get_category(cls):  # Class method (accesses static variable)
        return f"Product category: {cls.category}"

# Calling class methods
print(Product.get_category())

# Modifying the class variable using a class method
Product.set_category("Home Appliances")
print(Product.get_category())