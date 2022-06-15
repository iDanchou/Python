age = input("What is your current age? ")


def life_in_weeks():
    days_alive = int(age) * 365
    days_90 = 90 * 365
    days_left = int(days_90) - int(days_alive)
    weeks_alive = int(age) * 52
    weeks_90 = 90 * 52
    weeks_left = int(weeks_90) - int(weeks_alive)
    months_alive = int(age) * 12
    months_90 = 90 * 12
    months_left = int(months_90) - int(months_alive)
    print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")


life_in_weeks()

