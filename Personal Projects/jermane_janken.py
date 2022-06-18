
# Import the random library for random number #
import random


# Function calc 0, we know player chose 0 (Rock) so handle all cases for com choice #
# Passed in players choice and computers choice #
def calc_0_winner(p1, com):
    # if p1 (0) is equal to computer choice, this handle the case of com picking 0/Rock #
    if p1 == com:
        # Both are 0/ Rock then it's a tie #
        who_won = "It is a tie! You chose Rock, Computer chose Rock"
        # Return message back to main for RPS_winner on line 88 #
        return who_won
    # if com - 2 is 0 then player wins, this handles the case of com picking 2/scissors #
    elif p1 == com - 2:
        # P1 is 0/Rock and com is Scissors/2 to make it through the elif statement #
        who_won = "Player Wins! You chose Rock, Computer chose Scissors"
        # Return message back to main for RPS_Winner on line 88 #
        return who_won
    # Handles last case for player choosing rock(0) and computer choosing paper(1)
    # No logic needed since this is last possible case we can assume it #
    else:
        who_won = "Computer Wins! You chose Rock, Computer chose Paper"
        # Return message back to main for RPS_Winner on line 88
        return who_won


# Function calc 1, we know player chose 1 (Paper) so handle all cases for com choice #
# Passed in players choice and computers choice #
def calc_1_winner(p1, com):
    # if p1 (1) is equal to computer choice, this handle the case of com picking 1/Paper #
    if p1 == com:
        # Both are paper, create message to return #
        who_won = "It is a tie! You chose Paper, Computer chose Paper"
        return who_won
    # Handles p1 being 1 and com being 0 based on logic to be true #
    elif com == p1 - 1:
        # comp is rock(0) since p1 is 1, and we say to be true com must be p1(1) - 1
        who_won = "Player Wins! You chose Paper, Computer chose Rock"
        return who_won
    # Last case is that computer is 2 while we know player is 1, no logic needed since its the last possible case
    # that could happen based off of player choosing 1. We addressed all possible cases above with the else and elif
    else:
        who_won = "Computer Wins! You chose Paper, Computer chose Scissors"
        return who_won
    # In each function only one of the statements will hold true, either the if, elif, or else. Regardless of
    # which one we will return the value of who_won back to the main body of code to be caught by the
    # variable RPS_Winner on line 91


# Using the above comments try and reason through this function for when player chooses 2 (Scissors) #
def calc_2_winner(p1, com):
    # What would com need to be to enter this if statement?
    if p1 == com:
        who_won = "It is a tie! You chose Scissors, Computer chose Scissors"
    # What would com need to be to enter this elif statement?
    elif com == p1 - 1:
        who_won = "Player Wins! You chose Scissors, Computer chose Paper"
    # What case is left for com to be knowing p1 is 2, and we've addressed the above 2 cases?
    else:
        who_won = "Computer Wins! You chose Scissors, Computer chose Rock"
    return who_won
# Quiz: What line and variable is who_won being returned to for the function calc_2_winner function? #


#  Main Body Code. Main body code is your code outside of the functions. This is the code that drives the
#  program. The program will NOT look at your functions until you call them in the main body.
#  The program follows the below code line by line, if the condition is met, until you tell it otherwise/ jump to
# a function

# To loop the game we implement a while loop, but first have to declare the variable, my variable play_again
# We assign it Y so that it holds the condition on line 76 true so that the program can enter the loop and execute #
# The game will loop only when play_again holds the value Y
play_again = 'Y'
while play_again == 'Y':
    # Get the player choice #
    player_choice = int(input("Welcome to Rock, Paper, Scissors. Press 0 for Rock, 1 for Paper, and 2 for Scissors: "))
    # Create option list for computer to randomly select #
    choice_list = [0, 1, 2]
    # Randomly select 0-2 and assign to computer_choice #
    computer_choice = random.choice(choice_list)
    # Cases depending on what the player chooses #
    # If player selected rock/0 then calc the calc_0 function to handle all cases for when player has rock/0
    if player_choice == 0:
        # At this time the program calls the function and then executes the function on line 7 with the passed in
        # parameters of player_choice and computer_choice
        # RPS_Winner is now catching the value of whatever variable we return, in this case who_won
        RPS_Winner = calc_0_winner(player_choice, computer_choice)
    elif player_choice == 1:
        # Quiz: At this time what line of code did the program jump to when player_choice is 1 (Paper)?
        RPS_Winner = calc_1_winner(player_choice, computer_choice)
    else:
        RPS_Winner = calc_2_winner(player_choice, computer_choice)
    # Print message and results of the game, remember RPS_Winner holds our who_won value/messaged we returned
    # from the function
    print("%s Thanks for playing!" % RPS_Winner)
    # Ask user if they want to play again #
    play_again = input("Do you want to play again, type 'Y' or ''N'? ")
    # Force user input to uppercase for while loop condition, we need capital Y to play again
    # If anything else is entered besides Y when the code goes back to line 72 the game ends
    # The indention keeps everything under the while loop, everything is indented/under the while loop line 72
    play_again = play_again.upper()
# Since, we are no longer under the indention/while loop
# The below code is to be executed once out of the while loop...Only way out of the while loop is for the
# user to input anything as long as it is not Y, that would make our condition false at line 72 resulting in the exit
# of the while loop
# User doesn't want to play any more message #
print("Hope you enjoyed the game, see you later!")

# There's 1 way to break this game/code...What is it? Hint: Think about user choice input #
