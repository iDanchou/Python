# If the bill is $150.00 split between 5 people with 12% tip
# Each person should pay (150.00 / 5) * 1.12 is the same as 150 * 0.12 added to 150
# Round the result of the split to two decimal places


def bill_split():
    print("Welcome to the Tip Calculator.")
    bill = input("What was the total bill? ")
    percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
    people = input("How many people are splitting the bill? ")
    tip = int(percentage) / 100
    tip_amount = float(bill) * float(tip)
    total_bill = float(tip_amount) + float(bill)
    split_amount = float(total_bill) / int(people)
    new_split = round(split_amount, 2)
    print(f"Each person should pay: {new_split}")


bill_split()
