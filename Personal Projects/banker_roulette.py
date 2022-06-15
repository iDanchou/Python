import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# splits everything around a comma and a space

billed = random.sample(names, 1)
# print(f"{billed} is going to buy the meal today!")

num_items = (len(names))
random_choice = random.randint(0, num_items - 1)
payer = names[random_choice]
# print(f"{payer} is going to buy the meal today!")

new_payer = random.choice(names)
print(f"{new_payer} is going to buy the meal today!")
