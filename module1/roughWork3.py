num = int(input("Enter a number : "))

# Separate each digit of a number and print it and check palindrome
rev = 0
temp = num

while num > 0:
    digit = num % 10
    print(digit, end=" ")
    num = num // 10
    rev = rev * 10 + digit

print()

if rev == temp:
    print(f"{temp} is palindrome")
else:
    print(f"{temp} is not palindrome")

# Simple guessing game

isCorrect = False

while isCorrect == False:
    guess = int(input("Guess the number : "))
    if guess == temp:
        isCorrect = True
        print("You are correct")
    else:
        print("Incorrect. Try again")
