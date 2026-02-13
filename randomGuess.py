# Random guess game

import random

num = random.randint(1, 100)

tries = 0

while True:
    guess = int(input("Guess a number between 1 to 100 : "))

    if guess == num:
        tries = tries + 1
        print(f"You guessed the correct number in {tries} tries.")
        break
    elif guess > num:
        tries = tries + 1
        print(f"Guess a number smaller than {guess}")
    else:
        tries = tries + 1
        print(f"Guess a number greater than {guess}")
