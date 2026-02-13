# Accept an integer and Print hello world n times
num = int(input("Enter a number : "))

for i in range(num):
    print("Hello World")

# Print natural number up to n
for i in range(1, num + 1):
    print(i)

# Reverse for loop. Print n to 1
for i in range(num, 0, -1):
    print(i)

# Take a number as input and print its table
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")

# Sum upto n terms
count = 0

for i in range(1, num + 1):
    count = count + i

print(f"Sum is {count}")

# Factorial of a number
result = 1

for i in range(1, num + 1):
    result = result * i

print(f"Factorial is {result}")
