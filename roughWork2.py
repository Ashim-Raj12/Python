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

print("----- String Questions -----")

# Reverse a string without using in build functions
random = input("Give a string to reverse : ")

rev_random = ""

for char in random:
    rev_random = char + rev_random

print(f"{rev_random} is reverse of {random}")

# Check for Palindrome
if random == rev_random:
    print(f"{random} is palindome")
else:
    print(f"{random} is not palindrome")

# Count all letters, digits, and special symbols from a given string
gibrish = "ahs49#$5vd h*90 65**9dbjk h $89.0%"

char = 0
number = 0
special = 0

for i in gibrish:
    if i.isalpha():
        char = char + 1
    elif i.isdigit():
        number = number + 1
    else:
        special = special + 1

print(f"The number of Characters in {gibrish} is : {char}")
print(f"The number of Digits in {gibrish} is : {number}")
print(f"The number of Special Character in {gibrish} is : {special}")
