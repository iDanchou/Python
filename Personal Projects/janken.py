import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
computer_choice = random.randint(0, 2)


def player_option():
    if player_choice == 0:
        print(rock)
    elif player_choice == 1:
        print(paper)
    else:
        print(scissors)


player_option()


def computer_option():
    if computer_choice == 0:
        print(f"Computer chose:\n{rock}")
    elif computer_choice == 1:
        print(f"Computer chose:\n{paper}")
    else:
        print(f"Computer chose:\n{scissors}")


computer_option()

if player_choice == 0 and computer_choice == 1:
    print("Paper beats Rock, you lose!")
elif player_choice == 1 and computer_choice == 2:
    print("Scissors beats Paper, you lose!")
elif player_choice == 2 and computer_choice == 0:
    print("Rock beats Scissors, you lose!")
elif player_choice == 0 and computer_choice == 2:
    print("Rock beats Scissors, you win!")
elif player_choice == 1 and computer_choice == 0:
    print("Paper beats Rock, you win!")
elif player_choice == 2 and computer_choice == 1:
    print("Scissors beats Paper, you win!")
else:
    print("It's a draw!")