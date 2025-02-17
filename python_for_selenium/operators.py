# operators.py - Guide to Operators in Python

# 1. Arithmetic Operators
x = 10
y = 3
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)  # Rounds down to nearest integer
print("Modulus:", x % y)  # Remainder of division
print("Exponentiation:", x ** y)  # x raised to the power of y

# 2. Comparison Operators
print("Equal:", x == y)
print("Not Equal:", x != y)
print("Greater Than:", x > y)
print("Less Than:", x < y)
print("Greater or Equal:", x >= y)
print("Less or Equal:", x <= y)

# 3. Logical Operators
a = True
b = False
print("Logical AND:", a and b)
print("Logical OR:", a or b)
print("Logical NOT:", not a)

# 4. Assignment Operators
z = 5
z += 2  # Equivalent to z = z + 2
print("z after += 2:", z)
z *= 3  # Equivalent to z = z * 3
print("z after *= 3:", z)

# 5. Bitwise Operators
p = 5  # 0b0101
q = 3  # 0b0011
print("Bitwise AND:", p & q)  # 0b0001
print("Bitwise OR:", p | q)   # 0b0111
print("Bitwise XOR:", p ^ q)  # 0b0110
print("Bitwise NOT of p:", ~p) # Inverts all bits
print("Left Shift:", p << 1)  # 0b1010
print("Right Shift:", p >> 1)  # 0b0010

# 6. Identity Operators
print("Is:", x is y)
print("Is Not:", x is not y)

# 7. Membership Operators
text = "Hello Python"
print("'H' in text:", 'H' in text)
print("'Z' not in text:", 'Z' not in text)