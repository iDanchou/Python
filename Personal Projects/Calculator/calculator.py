from calculator_art import logo

print(logo)


def choose_calc():
    option = str(input("""\nWould you like to use:
(A). Addition:
(B). Subtraction:
(C). Multiplication:
(D). Division
Please enter an option: """))
    if option.lower() == "a":
        addition()
    elif option.lower() == "b":
        subtraction()
    elif option.lower() == "c":
        multiplication()
    elif option.lower() == "d":
        division()
    else:
        print("That doesn't look like one of the options. Please enter a valid choice.")
        choose_calc()


def addition():
    while True:
        try:
            num1 = float(input("\nEnter your 1st number for Addition: "))
            break
        except ValueError:
            print("This was not valid input. Please try again.")
    while True:
        try:
            num2 = float(input("Enter your 2nd number for Addition: "))
            break
        except ValueError:
            print("This was not valid input. Please try again.")
    print(num1 + num2)
    go_again()


def subtraction():
    while True:
        try:
            num1 = float(input("\nEnter your 1st number for Subtraction: "))
            break
        except ValueError:
            print("This was not valid input. Please try again.")
    while True:
        try:
            num2 = float(input("Enter your 2nd number for  Subtraction: "))
            break
        except ValueError:
            print("This was not valid input. Please try again.")
    print(num1 - num2)
    go_again()


def multiplication():
    while True:
        try:
            num1 = float(input("\nEnter your 1st number for Multiplication: "))
            break
        except ValueError:
            print("This was not valid input. Please try again.")
    while True:
        try:
            num2 = float(input("Enter your 2nd number for Multiplication: "))
            break
        except ValueError:
            print("This was not valid input. Please try again.")
    print(num1 * num2)
    go_again()


def division():
    while True:
        try:
            num1 = float(input("\nEnter the 1st number you wish to Divide: "))
            break
        except ValueError:
            print("This was not valid input. Please try again.")
    while True:
        try:
            num2 = float(input("Enter the 2nd number you wish to Divide: "))
            break
        except ValueError:
            print("This was not valid input. Please try again.")
    print(num1/num2)
    go_again()


def go_again():
    again = str(input("Would you like to perform any other functions? Press y to continue or q to quit: "))
    if again.lower() == "y":
        choose_calc()
    elif again.lower() == "q":
        print("Thanks for coming!")
    else:
        print("Please enter a valid option.")
        go_again()


print("Welcome.")
choose_calc()
