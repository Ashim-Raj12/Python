# ======================================
# TAKING INPUT FROM USER
# ======================================

numA = float(input("Enter number 1: "))
numB = float(input("Enter number 2: "))

print(f"\nNumber 1 is: {numA}")
print(f"Number 2 is: {numB}")


# ======================================
# ARITHMETIC OPERATORS
# ======================================

print("\n===== ARITHMETIC OPERATIONS =====")

print(f"Sum: {numA + numB}")
print(f"Difference: {numA - numB}")
print(f"Product: {numA * numB}")

# Avoid division by zero error
if numB != 0:
    print(f"Quotient: {numA / numB}")
    print(f"Remainder: {numA % numB}")
else:
    print("Cannot divide by zero!")

print(f"{numA} raised to the power {numB}: {numA ** numB}")


# ======================================
# COMPARISON OPERATORS
# ======================================

print("\n===== COMPARISON OPERATORS =====")

print(f"{numA} > {numB} : {numA > numB}")
print(f"{numA} < {numB} : {numA < numB}")
print(f"{numA} >= {numB} : {numA >= numB}")
print(f"{numA} <= {numB} : {numA <= numB}")
print(f"{numA} == {numB} : {numA == numB}")
print(f"{numA} != {numB} : {numA != numB}")


# ======================================
# LOGICAL OPERATORS
# ======================================

print("\n===== LOGICAL OPERATORS =====")

# Example conditions
condition1 = numA > 0
condition2 = numB > 0

print(f"numA > 0 AND numB > 0 : {condition1 and condition2}")
print(f"numA > 0 OR numB > 0  : {condition1 or condition2}")
print(f"NOT (numA > 0) : {not condition1}")


# ======================================
# PRACTICAL CONDITION CHECK
# ======================================

print("\n===== PRACTICAL CHECK =====")

if numA > numB:
    print("Number 1 is greater than Number 2")
elif numA < numB:
    print("Number 2 is greater than Number 1")
else:
    print("Both numbers are equal")
