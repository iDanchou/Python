import random

guesses = 0

name = input("Enter your name: ")

secret = random.randint(1, 100)
print(f"Hello {name}, I'm thinking of a number 1-100. See if you can guess it.\n")

while guesses < 9999:
    print("Take your best guess!")
    guess = input(": ")
    guess = int(guess)

    guesses = guesses + 1

    if guess < secret:
        print(f"{guess} is too low! Go higher.")

    if guess > secret:
        print(f"{guess} is too high! Go lower.")

    if guess == secret:
        print(f"{name} you got it! {guess} was right!")
        break
