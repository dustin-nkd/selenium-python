# type_of_inheritance.py

# 1. Single Inheritance
print("Example 1: Single Inheritance")

class Animal:
    def __init__(self, name):
        self.name = name  # Instance variable

    def speak(self):
        return "Some generic sound"

class Dog(Animal):  # Single inheritance
    def speak(self):
        return "Woof! Woof!"

# Creating an object
dog1 = Dog("Buddy")
print(f"{dog1.name} says: {dog1.speak()}")


# 2. Multiple Inheritance
print("\nExample 2: Multiple Inheritance")

class Swimmer:
    def swim(self):
        return f"{self.name} is swimming."

class Bird(Animal):
    def fly(self):
        return f"{self.name} is flying."

class Duck(Bird, Swimmer):  # Multiple inheritance
    def speak(self):
        return "Quack! Quack!"

# Creating an object
duck1 = Duck("Daffy")
print(f"{duck1.name} says: {duck1.speak()}, {duck1.fly()}, and {duck1.swim()}")


# 3. Multilevel Inheritance
print("\nExample 3: Multilevel Inheritance")

class Mammal(Animal):
    def has_fur(self):
        return f"{self.name} has fur."

class Cat(Mammal):
    def speak(self):
        return "Meow!"

# Creating an object
cat1 = Cat("Whiskers")
print(f"{cat1.name} says: {cat1.speak()} and {cat1.has_fur()}")


# 4. Hierarchical Inheritance
print("\nExample 4: Hierarchical Inheritance")

class Horse(Animal):
    def speak(self):
        return "Neigh!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

# Creating objects
horse1 = Horse("Spirit")
cow1 = Cow("Bessie")

print(f"{horse1.name} says: {horse1.speak()}")
print(f"{cow1.name} says: {cow1.speak()}")


# 5. Hybrid Inheritance (Combination of Multiple and Multilevel Inheritance)
print("\nExample 5: Hybrid Inheritance")

class Vehicle:
    def general_info(self):
        return "Vehicles are used for transportation."

class LandVehicle(Vehicle):
    def drive(self):
        return "This land vehicle is driving."

class WaterVehicle(Vehicle):
    def sail(self):
        return "This water vehicle is sailing."

class AmphibiousVehicle(LandVehicle, WaterVehicle):  # Hybrid inheritance
    def special_ability(self):
        return "This vehicle can both drive and sail!"

# Creating an object
amphibious1 = AmphibiousVehicle()
print(amphibious1.general_info())
print(amphibious1.drive())
print(amphibious1.sail())
print(amphibious1.special_ability())