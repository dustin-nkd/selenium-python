# super.py

# 1. Using `super()` to Call Parent Class Constructor
print("Example 1: Using `super()` to Call Parent Constructor")

class Animal:
    def __init__(self, name):
        self.name = name  # Instance variable

    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calling parent class constructor
        self.breed = breed  # Additional attribute in child class

    def speak(self):
        return "Woof! Woof!"

# Creating an object
dog1 = Dog("Buddy", "Golden Retriever")
print(f"{dog1.name} is a {dog1.breed} and says: {dog1.speak()}")


# 2. Using `super()` to Call Parent Method
print("\nExample 2: Using `super()` to Call Parent Method")

class Bird(Animal):
    def speak(self):
        parent_sound = super().speak()  # Calling the parent method
        return f"{parent_sound} (but I am a bird, so I chirp too!)"

# Creating an object
bird1 = Bird("Parrot")
print(f"{bird1.name} says: {bird1.speak()}")


# 3. `super()` in Multilevel Inheritance
print("\nExample 3: `super()` in Multilevel Inheritance")

class Mammal(Animal):
    def __init__(self, name, has_fur):
        super().__init__(name)  # Calling Animal's constructor
        self.has_fur = has_fur

class Cat(Mammal):
    def __init__(self, name, has_fur, breed):
        super().__init__(name, has_fur)  # Calling Mammal's constructor
        self.breed = breed

    def speak(self):
        return "Meow!"

# Creating an object
cat1 = Cat("Whiskers", True, "Siamese")
print(f"{cat1.name} is a {cat1.breed}, has fur: {cat1.has_fur}, and says: {cat1.speak()}")


# 4. `super()` in Multiple Inheritance
print("\nExample 4: `super()` in Multiple Inheritance")

class A:
    def show(self):
        return "Class A method"

class B(A):
    def show(self):
        return "Class B method"

class C(B):
    def show(self):
        return super().show()  # Calls the method from class B

# Creating an object
c1 = C()
print(c1.show())  # Calls `show()` from B


# 5. `super()` in Diamond Problem (Method Resolution Order - MRO)
print("\nExample 5: `super()` in Diamond Problem (MRO)")

class X:
    def show(self):
        return "Class X method"

class Y(X):
    def show(self):
        return "Class Y method"

class Z(X):
    def show(self):
        return "Class Z method"

class W(Y, Z):  # Multiple Inheritance
    def show(self):
        return super().show()  # Calls `show()` from Y first due to MRO

# Creating an object
w1 = W()
print(w1.show())  # Output will be from class Y due to MRO