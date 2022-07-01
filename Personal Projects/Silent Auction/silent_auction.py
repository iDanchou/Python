from silent_auction_art import logo

print(logo)

guests = {}
keep_going = True


while keep_going:
    guest = input("What is your name? ")
    bid = int(input("What is your bidding price? "))
    guests[guest] = bid
    more_guests = input("Are there any other bidders? ")
    if more_guests == "no":
        keep_going = False
    else:
        print("\n" * 80)

highest_bid = max(guests, key=guests.get)
print(f"The winner is {highest_bid} with the highest bid!")
