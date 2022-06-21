height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


def bmi_funct():
    bmi = float(weight) / float(height) ** 2
    new_bmi = round(bmi)
    if bmi < 18.5:
        print(f"Your BMI is {new_bmi}, you are underweight.")
    elif 18.5 < bmi < 25:
        print(f"Your BMI is {new_bmi}, you have a normal weight.")
    elif 25 < bmi < 30:
        print(f"Your BMI is {new_bmi}, you are slightly overweight.")
    elif 30 < bmi < 35:
        print(f"Your BMI is {new_bmi}, you are obese.")
    else:
        print(f"Your BMI is {new_bmi}, you are clinically obese.")


bmi_funct()
