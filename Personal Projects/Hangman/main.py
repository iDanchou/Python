import random
from hangman_words import word_list
from hangman_art import stages
import hangman_logo

print(hangman_logo.logo)

lives = 6


chosen_word = random.choice(word_list)

word_container = []
used_letters = []
for i in range(len(chosen_word)):
    word_container.append("_")

while "".join(word_container) != chosen_word:
    guess = input("\nGuess a letter: ").lower()
    if guess != chosen_word:
        used_letters.append(guess)
        print(used_letters)
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            word_container[i] = guess
    if guess not in chosen_word:
        lives -= 1
        print("That letter doesn't belong in this word! Guess again.")
    if lives == 6:
        print(stages[6])
    elif lives == 5:
        print(stages[5])
    elif lives == 4:
        print(stages[4])
    elif lives == 3:
        print(stages[3])
    elif lives == 2:
        print(stages[2])
    elif lives == 1:
        print(stages[1])
    else:
        print(stages[0])
    if lives == 0:
        print(f"The word was {chosen_word}")
        print("You lose!")
    print(word_container)

    if "".join(word_container) == chosen_word:
        print(f"\nThe word was {chosen_word}")
        print("\nYou win!")


