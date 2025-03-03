# inheritance.py

# 1. Basic Inheritance
print("Example 1: Basic Inheritance")

class Animal:
    def __init__(self, name):
        self.name = name  # Instance variable

    def make_sound(self):
        return "Some generic sound"

# Child class (inherits from Animal)
class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

# Creating objects
animal1 = Animal("Unknown Animal")
dog1 = Dog("Buddy")

print(f"{animal1.name} makes sound: {animal1.make_sound()}")
print(f"{dog1.name} makes sound: {dog1.make_sound()}")


# 2. Using the `super()` Function
print("\nExample 2: Using `super()` to Call Parent Constructor")

class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)  # Call parent constructor
        self.can_fly = can_fly  # Additional attribute in child class

    def make_sound(self):
        return "Chirp! Chirp!"

# Creating an object
bird1 = Bird("Parrot", True)
print(f"{bird1.name} can fly: {bird1.can_fly}, and it makes sound: {bird1.make_sound()}")


# 3. Multiple Levels of Inheritance
print("\nExample 3: Multilevel Inheritance")

class Mammal(Animal):
    def __init__(self, name, has_fur):
        super().__init__(name)
        self.has_fur = has_fur

class Cat(Mammal):
    def __init__(self, name, has_fur, breed):
        super().__init__(name, has_fur)
        self.breed = breed

    def make_sound(self):
        return "Meow!"

# Creating an object
cat1 = Cat("Whiskers", True, "Siamese")
print(f"{cat1.name} is a {cat1.breed}, has fur: {cat1.has_fur}, and makes sound: {cat1.make_sound()}")


# 4. Multiple Inheritance
print("\nExample 4: Multiple Inheritance")

class Swimmer:
    def __init__(self, name):
        self.name = name

    def swim(self):
        return f"{self.name} is swimming!"

class Fish(Animal, Swimmer):  # Inheriting from two classes
    def make_sound(self):
        return "Blub Blub!"

# Creating an object
fish1 = Fish("Goldfish")
print(f"{fish1.name} makes sound: {fish1.make_sound()} and {fish1.swim()}")


# 5. Method Overriding
print("\nExample 5: Overriding Methods")

class Vehicle:
    def move(self):
        return "The vehicle is moving"

class Car(Vehicle):
    def move(self):  # Overriding parent method
        return "The car is driving"

# Creating objects
vehicle1 = Vehicle()
car1 = Car()

print(vehicle1.move())
print(car1.move())


# 6. The `isinstance()` and `issubclass()` Functions
print("\nExample 6: Checking Inheritance with `isinstance()` and `issubclass()`")

print(isinstance(dog1, Animal))  # True, because Dog inherits from Animal
print(isinstance(dog1, Dog))  # True
print(isinstance(dog1, Bird))  # False

print(issubclass(Dog, Animal))  # True
print(issubclass(Bird, Animal))  # True
print(issubclass(Cat, Bird))  # False