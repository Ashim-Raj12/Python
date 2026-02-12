# Q1. Accept two numbers and print the greatest between them.

numA = int(input("Enter Number 1 : "))
numB = int(input("Enter Number 2 : "))

if numA > numB:
    print(f"{numA} is greater than {numB}")
elif numB > numA:
    print(f"{numB} is greater than {numA}")
else:
    print(f"{numA} is equal to {numB}")
