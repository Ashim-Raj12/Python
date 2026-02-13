# Loops

# For Loop -- Printing table of the user input
num = int(input("Enter a number : "))

for i in range(1, 11, 1):
    print(f"{num} * {i} = {num * i}")

numA = int(input("Enter another number : "))

for i in range(0, numA, 2):
    print(i)
