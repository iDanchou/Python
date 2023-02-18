from blackjack_art import logo
import random

print(logo)

# face_cards = {"J": 10, "Q": 10, "K": 10}
# face_cards = list(face_cards.values())


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_hand = random.sample(cards, 2)
    final_player_hand = sum(player_hand)
    opponent_hand = random.choice(cards)
    print(f"Your cards: {player_hand}, current score: {final_player_hand}")
    print(f"Opponent's first card: {opponent_hand}")
    opponent_hand += random.choice(cards)
    final_opponent_hand = sum(opponent_hand)

    extra_card = True

    while extra_card:
        want_card = input("Would you like another card? ")
        if want_card == "yes":
            player_hand += random.choice(cards)

    if final_opponent_hand < 17:
        final_opponent_hand += random.choice(cards)

    if final_player_hand == 21:
        print("BLACKJACK! You've won!")
    elif final_opponent_hand == 21:
        print("BLACKJACK! You've lost!")
    elif final_player_hand > 21:
        print("BUST. Opponent has won.")
    elif final_opponent_hand > 21:
        print("BUST. Player has won.")
    elif final_player_hand > final_opponent_hand:
        print("You win!")
    elif final_player_hand < final_opponent_hand:
        print("You lose!")
    else:
        print("It's a draw")


deal_card()
