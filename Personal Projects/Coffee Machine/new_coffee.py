from coffee_data import resources, MENU

# Defining all pertinent variables
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01
total_inserted = 0

# Everything needed to make espresso
espresso_price = MENU['espresso']['cost']
espresso_water = MENU['espresso']['ingredients']['water']
espresso_coffee = MENU['espresso']['ingredients']['coffee']

# Everything needed to make latte
latte_price = MENU['latte']['cost']
latte_water = MENU['latte']['ingredients']['water']
latte_milk = MENU['latte']['ingredients']['milk']
latte_coffee = MENU['latte']['ingredients']['coffee']

# Everything needed to make cappuccino
cappuccino_price = MENU['cappuccino']['cost']
cappuccino_water = MENU['cappuccino']['ingredients']['water']
cappuccino_milk = MENU['cappuccino']['ingredients']['milk']
cappuccino_coffee = MENU['cappuccino']['ingredients']['coffee']

# All remaining resources within the machine
remaining_water = resources['water']
remaining_milk = resources['milk']
remaining_coffee = resources['coffee']
change = 0
money_in_machine = 0

order = input("What would you like? (espresso/latte/cappuccino): ").lower()


# TODO: 1. Prompt user for input
def take_order():
    """Accepts user input and will operate based on command"""
    if order == "report":
        print_report()
    elif order == "off":
        machine_off()

    elif order == "espresso":
        can_make_espresso()

    elif order == "latte":
        can_make_latte()

    elif order == "cappuccino":
        can_make_cappuccino()

    else:
        print("\nPlease choose one of the options.")
        take_order()


# TODO: 2. Turn off coffee machine
def machine_off():
    """Will exit program"""
    exit()


# TODO: 3 Print report
def print_report():
    """Will print all available resources within the machine"""
    print(f"Water: {remaining_water}ml")
    print(f"Milk: {remaining_milk}ml")
    print(f"Coffee: {remaining_coffee}ml")
    print(f"Money: ${money_in_machine}")


# TODO: 4. Check resources sufficient
def can_make_espresso():
    """Will check if resources are available to make espresso"""
    if remaining_water > espresso_water:

        if remaining_coffee > espresso_coffee:

            process_coins()
        else:
            print("Sorry, there is not enough coffee.")
    else:
        print("Sorry there is not enough water.")


def can_make_latte():
    """Will check if resources are available to make latte"""
    if remaining_water > latte_water:

        if remaining_coffee > latte_coffee:

            if remaining_milk > latte_milk:

                process_coins()
            else:
                print("Sorry, there is not enough milk.")
        else:
            print("Sorry, there is not enough coffee.")
    else:
        print("Sorry, there is not enough water.")


def can_make_cappuccino():
    """Will check if resources are available to make cappuccino"""
    if remaining_water > cappuccino_water:

        if remaining_coffee > cappuccino_coffee:

            if remaining_milk > cappuccino_milk:

                process_coins()
            else:
                print("Sorry, there is not enough milk.")
        else:
            print("Sorry, there is not enough coffee.")
    else:
        print("Sorry, there is not enough water.")


# TODO: 5. Process coins
def process_coins():
    """Takes user input to calculate total amount entered into the machine"""
    global change
    global money_in_machine
    global total_inserted

    print("Please insert coins.")

    quarters_inserted = int(input("How many quarters: "))
    quarters_total = quarters_inserted * quarters

    dimes_inserted = int(input("How many dimes: "))
    dimes_total = dimes_inserted * dimes

    nickles_inserted = int(input("How many nickles: "))
    nickles_total = nickles_inserted * nickles

    pennies_inserted = int(input("How many pennies: "))
    pennies_total = pennies_inserted * pennies

    total_inserted += quarters_total + nickles_total + dimes_total + pennies_total
    total_inserted = round(total_inserted, 2)

    if order == "espresso":
        espresso_money()
    elif order == "latte":
        latte_money()
    elif order == "cappuccino":
        cappuccino_money()


# TODO: 6. Check transaction successful
def espresso_money():

    global money_in_machine
    global change

    if total_inserted == espresso_price:
        making_espresso()

    elif total_inserted > espresso_price:
        money_in_machine += total_inserted
        change += money_in_machine - espresso_price
        round(change, 2)
        print(f"\nHere is ${change} in change")
        making_espresso()

    elif total_inserted < espresso_price:
        print("\nSorry, that's not enough money. Money refunded.")
        process_coins()


def latte_money():

    global money_in_machine
    global change

    if total_inserted == latte_price:
        making_latte()

    elif total_inserted > latte_price:
        money_in_machine += total_inserted
        change += money_in_machine - latte_price
        round(change, 2)
        print(f"\nHere is ${change} in change")
        making_latte()

    elif total_inserted < latte_price:
        print("\nSorry, that's not enough money. Money refunded.")
        process_coins()


def cappuccino_money():

    global money_in_machine
    global change

    if total_inserted == cappuccino_price:
        making_cappuccino()

    elif total_inserted > cappuccino_price:
        money_in_machine += total_inserted
        change += money_in_machine - cappuccino_price
        round(change, 2)
        print(f"\nHere is ${change} in change")
        making_cappuccino()

    elif total_inserted < cappuccino_price:
        print("\nSorry, that's not enough money. Money refunded.")
        process_coins()


def making_espresso():

    global remaining_water
    global remaining_coffee

    remaining_coffee -= espresso_coffee
    remaining_water -= espresso_water
    print("\nHere is your espresso. Enjoy!")
    take_order()


def making_latte():

    global remaining_water
    global remaining_coffee
    global remaining_milk

    remaining_coffee -= latte_coffee
    remaining_water -= latte_water
    remaining_milk -= latte_milk
    print("\nHere is your latte. Enjoy!")
    take_order()


def making_cappuccino():

    global remaining_water
    global remaining_coffee
    global remaining_milk

    remaining_coffee -= cappuccino_coffee
    remaining_water -= cappuccino_water
    remaining_milk -= cappuccino_milk
    print("\nHere is your cappuccino. Enjoy!")
    take_order()


take_order()
