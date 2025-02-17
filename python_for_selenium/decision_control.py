# decision_control.py

# 1. Basic if-else statement
x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")

# 2. if-elif-else statement
y = 20

if y < 10:
    print("y is less than 10")
elif y == 10:
    print("y is equal to 10")
else:
    print("y is greater than 10")

# 3. Checking multiple conditions (logical operators)
z = 15

if 10 < z < 20:
    print("z is between 10 and 20")

if z == 15 or z == 20:
    print("z is either 15 or 20")

if not (z == 10):
    print("z is not 10")

# 4. Conditional statement with string variable
color = "blue"

if color == "red":
    print("The color is red")
elif color == "green":
    print("The color is green")
else:
    print("The color is neither red nor green")