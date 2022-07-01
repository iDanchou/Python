print("Welcome to the Love Calculator!")
name1 = input("What is your name?: ")
name2 = input("What is their name?: ")


def love_score():
    new_name1 = name1.lower()
    new_name2 = name2.lower()

    num_t = int(new_name1.count("t")) + int(new_name2.count("t"))
    num_r = int(new_name1.count("r")) + int(new_name2.count("r"))
    num_u = int(new_name1.count("u")) + int(new_name2.count("u"))
    num_e = int(new_name1.count("e")) + int(new_name2.count("e"))
    num_l = int(new_name1.count("l")) + int(new_name2.count("l"))
    num_o = int(new_name1.count("o")) + int(new_name2.count("o"))
    num_v = int(new_name1.count("v")) + int(new_name2.count("v"))

    true_name_score = int(num_t) + int(num_r) + int(num_u) + int(num_e)
    love_name_score = int(num_l) + int(num_o) + int(num_v) + int(num_e)

    true_love_score = str(true_name_score) + str(love_name_score)

    if int(true_love_score) < 10 or int(true_love_score) > 90:
        print(f"Your score is {true_love_score}, you go together like coke and mentos.")
    elif 39 < int(true_love_score) < 51:
        print(f"Your score is {true_love_score}, you are alright together.")
    else:
        print(f"Your score is {true_love_score}.")


love_score()

