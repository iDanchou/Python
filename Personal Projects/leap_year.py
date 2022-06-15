year = int(input("Which year do you want to check? "))


def leap_year():
    if year % 4 == 0:
        if year % 100 != 0:
            print("Leap year.")
        elif year % 100 == 0 and year % 400 == 0:
            print("Leap year.")
        elif year % 100 == 0 and year % 400 != 0:
            print("Not leap year")
        elif year % 100 != 0 and year % 400 == 0:
            print("Leap year.")
    else:
        print("Not leap year.")


# leap_year()


def leap_year_2():
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year")
            else:
                print("Not leap year")
        else:
            print("Leap year")
    else:
        print("Not a leap year")

# leap_year_2


def leap_year_3():
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year")
    else:
        print("Not leap year")


# leap_year_3()
