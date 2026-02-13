# ==============================
# BASIC PRINTING IN PYTHON
# ==============================

print("Hello World!!")

"""
This is a multi-line comment (Docstring).
Docstrings are usually used to describe
functions, classes, or modules.
"""

# ==============================
# VARIABLES & DATA TYPES
# ==============================

# Python is dynamically typed → No need to define type manually

name = "Ashim"  # String
age = 21  # Integer
weight = 48.67  # Float
complex_num = 34j  # Complex number
in_college = True  # Boolean (True / False)

# Printing multiple variables
print(name, age, weight, complex_num, in_college)

# f-string (Best and modern way to format strings)
print(f"My name is {name}, age is {age}, weight is {weight} kg.")
print(f"Am I in college? {in_college}")

# Checking type of a variable
print("Type of name is:", type(name))


# ==============================
# STRINGS IN PYTHON
# ==============================

a = "A"
unicode_number = 128522  # Unicode for 😊

# ord() → Character to Unicode
print("Unicode of 'A':", ord(a))

# chr() → Unicode to Character
print("Character of 128522:", chr(unicode_number))

nameA = "Ashim Raj"

# Indexing (Accessing characters)
print("First character:", nameA[0])  # A
print("Last character:", nameA[-1])  # j

# Slicing → [start : end : step]
first_name = nameA[0:5:1]  # Ashim
last_name = nameA[6:9:1]  # Raj

print("First Name:", first_name)
print("Last Name:", last_name)


# ==============================
# TYPE CONVERSION (TYPE CASTING)
# ==============================

# int → str
numA = 67
numA_str = str(numA)
print("Converted int to string:", numA_str, type(numA_str))

# str → int
numB = "67"
numB_int = int(numB)
print("Converted string to int:", numB_int, type(numB_int))

# int → float
numC = 10
numC_float = float(numC)
print("Converted int to float:", numC_float, type(numC_float))

# float → int (Removes decimal part)
numD = 45.89
numD_int = int(numD)
print("Converted float to int:", numD_int, type(numD_int))

# int → complex
numE = 5
numE_complex = complex(numE)
print("Converted int to complex:", numE_complex, type(numE_complex))

# complex → string
numF = 3 + 4j
numF_str = str(numF)
print("Converted complex to string:", numF_str, type(numF_str))

# bool() converts values based on truthiness

print("bool(1):", bool(1))  # True
print("bool(0):", bool(0))  # False
print("bool(100):", bool(100))  # True
print("bool(-5):", bool(-5))  # True

print("bool('Hello'):", bool("Hello"))  # True
print("bool(''):", bool(""))  # False (empty string)

print("bool(0.0):", bool(0.0))  # False
print("bool(3.14):", bool(3.14))  # True

print("bool([]):", bool([]))  # False (empty list)
print("bool([1,2,3]):", bool([1, 2, 3]))  # True

# Unicode conversion
char_example = "B"
unicode_value = ord(char_example)
print("Unicode of B:", unicode_value)

unicode_to_char = chr(66)
print("Character of 66:", unicode_to_char)
