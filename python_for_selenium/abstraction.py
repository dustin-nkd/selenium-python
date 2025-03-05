# abstraction.py

from abc import ABC, abstractmethod

# 1. Understanding Abstraction using Abstract Base Classes (ABC)
print("Example 1: Using Abstract Base Class (ABC)")

class Animal(ABC):  # Abstract Base Class
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):  # Abstract method (must be implemented in child classes)
        pass

class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creating objects
dog1 = Dog("Buddy")
cat1 = Cat("Whiskers")

print(f"{dog1.name} says: {dog1.speak()}")
print(f"{cat1.name} says: {cat1.speak()}")

# 2. Abstraction in Action - Preventing Direct Instantiation
print("\nExample 2: Preventing Direct Instantiation of Abstract Class")

try:
    animal1 = Animal("Some Animal")  # This will raise an error
except TypeError as e:
    print(f"Error: {e}")


# 3. Partial Abstraction - Abstract Class with Concrete Method
print("\nExample 3: Abstract Class with Concrete Method")

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    def general_info(self):  # Concrete method (not abstract)
        return "Vehicles are used for transportation."

    @abstractmethod
    def fuel_type(self):  # Abstract method
        pass

class Car(Vehicle):
    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Vehicle):
    def fuel_type(self):
        return "Electric Battery"

# Creating objects
car1 = Car("Toyota")
ev1 = ElectricCar("Tesla")

print(f"{car1.brand}: {car1.general_info()}, Fuel: {car1.fuel_type()}")
print(f"{ev1.brand}: {ev1.general_info()}, Fuel: {ev1.fuel_type()}")