# Loops

# For Loop
num = int(input("Enter a number : "))

for i in range(1, 11, 1):
    print(f"{num} * {i} = {num * i}")

for i in range(0, num, 2):
    print(i)

# For Loops for String
name = "Ashim Raj"

for i in range(0, len(name), 2):
    print(name[i])

for char in name:
    print(char)
