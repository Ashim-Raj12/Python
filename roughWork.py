# Q1. Accept two numbers and print the greatest between them.

numA = int(input("Enter Number 1 : "))
numB = int(input("Enter Number 2 : "))

if numA > numB:
    print(f"{numA} is greater than {numB}")
elif numB > numA:
    print(f"{numB} is greater than {numA}")
else:
    print(f"{numA} is equal to {numB}")

# Q2. Accept the gender from the user as char and print the respective greeting message .Ex - Good Morning Sir (on the basis of gender)

gender = input("Enter F or M as your gender : ").strip().upper()

if gender == "M":
    print("Good Morning Sir")
elif gender == "F":
    print("Good Morning Mam")
else:
    print("Please Enter a valid gender")
    print("Restart to see results")

# Q3. Accept an integer and check whether it is an even number or odd.

num = int(input("Enter an integer : "))

if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")
