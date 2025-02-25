# self.py

# 1. Understanding the `self` parameter in a class
print("Example 1: Using `self` to access instance attributes")

class Person:
    def __init__(self, name, age):
        self.name = name  # `self.name` refers to the instance attribute
        self.age = age    # `self.age` refers to the instance attribute

    def introduce(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old."

# Creating an object
person1 = Person("Alice", 25)
print(person1.introduce())

# `self` ensures that each object has its own unique attributes
person2 = Person("Bob", 30)
print(person2.introduce())


# 2. `self` must be used inside instance methods
print("\nExample 2: Modifying attributes using `self`")

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def update_model(self, new_model):
        self.model = new_model  # `self.model` ensures we modify the instance attribute

    def display_info(self):
        return f"Car: {self.brand} {self.model}"

# Creating an object
car1 = Car("Toyota", "Corolla")
print(car1.display_info())

# Updating the model
car1.update_model("Camry")
print("After updating model:", car1.display_info())


# 3. `self` differentiates instance attributes from method parameters
print("\nExample 3: `self` avoids confusion between instance attributes and method parameters")

class Rectangle:
    def __init__(self, width, height):
        self.width = width  # `self.width` is the instance attribute
        self.height = height  # `self.height` is the instance attribute

    def area(self):
        return self.width * self.height  # Uses `self` to refer to the object's attributes

# Creating an object
rect1 = Rectangle(10, 5)
print(f"Rectangle Area: {rect1.area()}")


# 4. Calling a method inside another method using `self`
print("\nExample 4: Using `self` to call another method")

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * 3.14159 * self.radius  # Uses `self.radius`

    def area(self):
        return 3.14159 * (self.radius ** 2)  # Uses `self.radius`

    def display_info(self):
        return f"Circle with radius {self.radius}: Area = {self.area()}, Circumference = {self.circumference()}"

# Creating an object
circle1 = Circle(7)
print(circle1.display_info())


# 5. `self` refers to the specific instance calling the method
print("\nExample 5: `self` allows multiple objects to store different data")

person3 = Person("Charlie", 22)
person4 = Person("David", 28)

print(person3.introduce())  # Uses `self` for the specific object
print(person4.introduce())  # Uses `self` for another object


# 6. `self` is not required for class methods (alternative to instance methods)
print("\nExample 6: Class method without `self` (using @staticmethod)")

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Calling the method without an instance
print(f"Addition: {MathUtils.add(5, 3)}")