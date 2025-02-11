# Toán tử số học (Arithmetic Operators)
a, b = 10, 3

print(a + b)  # Cộng: 13
print(a - b)  # Trừ: 7
print(a * b)  # Nhân: 30
print(a / b)  # Chia: 3.3333
print(a // b)  # Chia lấy nguyên: 3
print(a % b)  # Chia lấy dư: 1
print(a ** b)  # Lũy thừa: 10^3 = 1000

# Toán tử so sánh (Comparison Operators)
print(a == b)  # False
print(a != b)  # True
print(a > b)  # True
print(a < b)  # False
print(a >= b)  # True
print(a <= b)  # False

# Toán tử gán (Assignment Operators)
x = 5
x += 3  # x = x + 3

print(x)  # 8

# Toán tử logic (Logical Operators)
x, y = True, False

print(x and y)  # False
print(x or y)  # True
print(not x)  # False

# Toán tử bitwise (Bitwise Operators)
a, b = 5, 3  # 5 = 101, 3 = 011

print(a & b)  # AND: 001 -> 1
print(a | b)  # OR:  111 -> 7
print(a ^ b)  # XOR: 110 -> 6
print(~a)  # NOT: -6
print(a << 1)  # Dịch trái: 1010 -> 10
print(a >> 1)  # Dịch phải: 10 -> 2

# Toán tử thành viên (Membership Operators)
numbers = [1, 2, 3, 4]

print(2 in numbers)  # True
print(5 not in numbers)  # True

# Toán tử danh tính (Identity Operators)
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True (cùng địa chỉ)
print(a is c)  # False (khác địa chỉ)
print(a == c)  # True (cùng giá trị)

# Toán tử ba ngôi (Ternary Operator)
x, y = 10, 20
min_value = x if x < y else y

print(min_value)  # 10