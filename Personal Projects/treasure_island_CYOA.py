print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


def forked_path():
    left_or_right = input("As you're walking, the trail opens to reveal a fork in the road.\nDo you choose to go left, or right?: ")
    if left_or_right.lower() == "left":
        wait_or_swim = input("You follow the path that leads to the left and you encounter a large river.\nThe water is rushing violently but you need to cross, do you wait or try and swim across?: ")
        if wait_or_swim.lower() == "wait":
            colored_door = input("You decide to wait for the water to calm and fortunately you notice a weathered piece of driftwood floating nearby.\nYou climb on and safely make your way across the water. You wash up on the shore and notice three large doors of varying colors.\nWhich do you choose? Red, Blue, or Yellow?: ")
            if colored_door.lower() == "yellow":
                print("As you push open the yellow doors you see pools of gold and treasures shining as far the eye can see. Congratulations!")
            else:
                print("As you push open the doors you feel something unpleasant waiting for you on the other side. A glint of metal reflects against the light but it's too late to react.\nThe trap had been triggered and arrows come flying from the wall ahead! Game Over!")
        else:
            print("You decide to take your chances and you plunge right into the water! Unfortunately the current was far too strong and you're whisked away downstream. Game Over!")
    else:
        print("You begin walking down the path on the right and you can feel something is amiss, however you noticed far too late. You step into a spike pit. Game Over!")


forked_path()