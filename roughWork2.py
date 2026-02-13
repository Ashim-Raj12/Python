# Accept an integer and Print hello world n times
num = int(input("Enter a number : "))

print(f"-----Hello World is printing {num} times-----")
for i in range(num):
    print("Hello World")

# Print natural number up to n
print(f"-----Printing upto {num}-----")
for i in range(1, num + 1):
    print(i)

# Reverse for loop. Print n to 1
print(f"-----Printing from {num} to 1-----")
for i in range(num, 0, -1):
    print(i)

# Take a number as input and print its table
print(f"-----Multiplication Table of {num}-----")
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

# Print the sum of all even & odd numbers in a range separately
odd_sum = 0
even_sum = 0

for i in range(1, num + 1):
    if i % 2 != 0:
        odd_sum = odd_sum + i
    else:
        even_sum = even_sum + i

print(f"Even Sum is : {even_sum}")
print(f"Odd sum is : {odd_sum}")

# Print all the factors of a number
print(f"-----Printing factors of {num}------")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)

# Check if it a perfect number or not
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum = sum + i

if sum == num:
    print(f"{num} is perfect number")
else:
    print(f"{num} is not a perfect number")

# Check wether the number is prime or not
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count = count + 1

if count > 2:
    print(f"{num} is Composite")
else:
    print(f"{num} is Prime")
