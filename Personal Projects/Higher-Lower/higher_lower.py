from HL_art import logo, vs
from HL_game_data import data
import random


def format_data(option):
    """Format the data for the accounts"""
    option_name = option['name']  # uses name key to find value
    option_description = option['description']  # Uses the description key to find the value
    option_country = option['country']   # uses the country key to find the value for each option
    option_followers = option['follower_count']  # uses the follower key to find the value for each option
    return f"{option_name}, {option_description}, from {option_country}."


def check_answer(answer, option_a_follower, option_b_follower):
    """Takes account data and returns if answer was correct"""
    if option_a_follower > option_b_follower:
        return answer == "A"
    else:
        return answer == "B"


# Display art
print(logo)

score = 0

again = True

option_b = random.choice(data)

while again:
    # Generate a random account from within the list
    option_a = option_b
    option_b = random.choice(data)
    if option_a == option_b:
        option_b = random.choice(data)

    print(f"compare A: {format_data(option_a)}.")
    print(vs)
    print(f"Against B: {format_data(option_b)}.")

    # Prompt user for the answer
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()

    option_a_follower = option_a['follower_count']
    option_b_follower = option_b['follower_count']

    is_correct = check_answer(answer, option_a_follower, option_b_follower)

    print(logo)

    if is_correct:
        score += 1
        print(f"You're right! Score count: {score}")
    else:
        print(f"Sorry, that's wrong! Final Score: {score}")
        again = False


# if answer == "a" and option_a_follower > option_b_follower:
#     score += 1
#     option_b = option_a
#     print(logo)
#     print(f"you're right! current score: {score}.")
#     option_a = random.choice(data)
#     print(f"compare a: {option_a_name}, {option_a_description}, from {option_a_country}.")
#     print(vs)
#     print(f"against b: {option_b_name}, {option_b_description}, from {option_b_country}.")
#     answer = input("who has more followers? type 'a' or 'b': ").upper()
# elif answer == "b" and option_b_followers > option_a_followers:
#     score += 1
#     option_a = random.choice(data)
#     print(logo)
#     print(f"you're right! current score: {score}.")
#     print(f"compare a: {option_a_name}, {option_a_description}, from {option_a_country}.")
#     print(vs)
#     print(f"against b: {option_b_name}, {option_b_description}, from {option_b_country}.")
#     answer = input("who has more followers? type 'a' or 'b': ").upper()
# else:
#     print(f"\nyou got that one wrong! your final score was {score}.")
#     play_again = input("\nwould you like to play again? type 'y' for yes and 'n' for no: ").upper()
#     if play_again == 'y':
#         score = 0
#         print(logo)
#         option_a = random.choice(data)
#         option_b = random.choice(data)
#         print(f"compare a: {option_a_name}, {option_a_description}, from {option_a_country}.")
#         print(vs)
#         print(f"against b: {option_b_name}, {option_b_description}, from {option_b_country}.")
#         answer = input("who has more followers? type 'a' or 'b': ").upper()
#     else:
#         exit()
#
