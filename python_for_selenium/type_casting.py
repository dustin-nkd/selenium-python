# type_casting.py - Guide to Type Casting in Python

# 1. Converting Integer to Float
num_int = 10
num_float = float(num_int)
print("Integer to Float:", num_float, "Type:", type(num_float))

# 2. Converting Float to Integer
num_float = 10.7
num_int = int(num_float)  # Truncates decimal part
print("Float to Integer:", num_int, "Type:", type(num_int))

# 3. Converting String to Integer
num_str = "123"
num_int = int(num_str)
print("String to Integer:", num_int, "Type:", type(num_int))

# 4. Converting String to Float
num_str = "123.45"
num_float = float(num_str)
print("String to Float:", num_float, "Type:", type(num_float))

# 5. Converting Integer to String
num_int = 100
num_str = str(num_int)
print("Integer to String:", num_str, "Type:", type(num_str))

# 6. Converting Boolean to Integer
is_python_fun = True
num_int = int(is_python_fun)
print("Boolean to Integer:", num_int, "Type:", type(num_int))

# 7. Converting Integer to Boolean
num_int = 0
bool_value = bool(num_int)  # False if 0, True otherwise
print("Integer to Boolean:", bool_value, "Type:", type(bool_value))