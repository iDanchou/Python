import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password: "))
nr_symbols = int(input(f"How many symbols would you like: "))
nr_numbers = int(input(f"How many numbers would you like: "))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# takes the value from nr_letters and chooses a random amount from the letters list
chosen_letters = random.choices(letters, k=nr_letters)
# joins the list of letters with no seperator
chosen_letters1 = "".join(chosen_letters)
# takes the value from nr_symbols and chooses a random amount from the symbols list
chosen_symbols = random.choices(symbols, k=nr_symbols)
# joins the list of symbols with no seperator
chosen_symbols1 = "".join(chosen_symbols)
# takes the value from nr_numbers and chooses a random amount from the numbers list
chosen_numbers = random.choices(numbers, k=nr_numbers)
# joins the list of numbers with no seperator
chosen_numbers1 = "".join(chosen_numbers)
# adding together the collected letters, numbers, and symbols into one variable
easy_password = chosen_letters1 + chosen_symbols1 + str(chosen_numbers1)
print(easy_password)

# Hard - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# converts easy password into a list
hard_password = list(easy_password)
# shuffles hard password
random.shuffle(hard_password)
# combines hard_password into a singular string
hard_password1 = "".join(hard_password)
print(hard_password1)
