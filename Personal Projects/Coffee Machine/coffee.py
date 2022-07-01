from coffee_data import MENU, resources

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01

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
money_in_machine = 0
change = 0

# Other variables that need to be assigned


# TODO: 2. Print report of all coffee machine resources
def report():
    print(f"Water: {remaining_water}ml")
    print(f"Milk: {remaining_milk}ml")
    print(f"Coffee: {remaining_coffee}ml")
    print(f"Money: ${money_in_machine}")


def insert_coins():
    print("Please insert coins.")
    quarters_inserted = int(input("How many quarters: "))
    dimes_inserted = int(input("How many dimes: "))
    nickles_inserted = int(input("How many nickles: "))
    pennies_inserted = int(input("How many pennies: "))
    quarters_total = quarters_inserted * quarters
    dimes_total = dimes_inserted * dimes
    nickles_total = nickles_inserted * nickles
    pennies_total = pennies_inserted * pennies
    total_inserted = quarters_total + nickles_total + dimes_total + pennies_total


def make_espresso(espresso_water, espresso_coffee, espresso_price, change, total_inserted):
    remaining_water -= remaining_water - espresso_water
    remaining_coffee -= remaining_coffee - espresso_coffee
    money_in_machine += espresso_price
    change += total_inserted - espresso_price
    return remaining_coffee, remaining_water, money_in_machine, change


def make_latte(remaining_water, remaining_coffee, remaining_milk, money_in_machine, change, total_inserted):
    remaining_water -= remaining_water - latte_water
    remaining_coffee -= remaining_coffee - latte_coffee
    remaining_milk -= remaining_milk - latte_milk
    money_in_machine += latte_price
    change += total_inserted - latte_price
    return remaining_coffee, remaining_water, remaining_milk, change


def make_cappuccino(remaining_water, remaining_coffee, remaining_milk, money_in_machine, change, total_inserted):
    remaining_water -= remaining_water - cappuccino_water
    remaining_coffee -= remaining_coffee - cappuccino_coffee
    remaining_milk -= remaining_milk - cappuccino_milk
    money_in_machine += cappuccino_price
    change += total_inserted - cappuccino_price
    return remaining_coffee, remaining_water, remaining_milk


# TODO: 1. Prompt user for coffee choice
def take_order():
    order = input("What would you like? (Espresso/Late/Cappuccino): ").lower()
    if order == "report":
        report()
    elif order == "espresso":
        make_espresso(espresso_water, espresso_coffee, money_in_machine, change, total_inserted)
        print("Please insert coins.")
        insert_coins()
    elif order == "latte":
        make_latte(remaining_water, remaining_coffee, remaining_milk, money_in_machine, change)
        print("Please insert coins.")
        insert_coins()
    elif order == "cappuccino":
        make_cappuccino(remaining_water, remaining_coffee, remaining_milk, money_in_machine, change)
        print("Please insert coins.")
        insert_coins()


# TODO: 3. Check resources sufficient


# TODO: 4. Process Coins


# TODO: 5. Check transaction successful


# TODO: 6. Make coffee
