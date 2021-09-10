# Andreina Harding
# this is the first project in python, a guessing a number game.

import random

LOWER_RANGE = 1
UPPER_RANGE = 10
high_score = 0

#Initial greeting of the game
def start_game():
    print("-"*95)
    print("\n Welcome to the Guessing A Number Game! \n")
    print("-"*95)
    print ("highscore: {}".format(high_score))
    return input("Enter a number between 1 and 10: ")

#Defines if the user_input is an integer, returns the integer or Cero
def is_a_number(the_user_input):
    is_number= False
    number=0
    try:
        int(the_user_input)
        is_number= True
    except ValueError:
        print("Oh no, that is not a valid entrance!")
    if  is_number:
         number= int(the_user_input)
    return  number
                                             
# Kick off the program by calling the start_game function.
user_input=start_game()
number_to_guess = random.randint(LOWER_RANGE, UPPER_RANGE)
game_continue = 'y'
attempts_counter=1
while game_continue.lower() == 'y':
    number=is_a_number(user_input)
    while number != number_to_guess:
        if number >  UPPER_RANGE or number < LOWER_RANGE:
            try:
                raise ValueError 
            except ValueError as err:
                print("The number must be in the 1 -10 range")

        if number < UPPER_RANGE and number > number_to_guess:
             print ("It is lower than {}".format(number))
        elif number >= LOWER_RANGE and number < number_to_guess:
             print ("It is bigger than {}".format(number))
        user_input= input("try again: ")
        attempts_counter += 1
        number=is_a_number(user_input)
    print("you got it!!!! {} was the number!! you used {} attempt(s)".format(number, attempts_counter))
    game_continue= input("Do you want to play again? ")
    if game_continue == 'y':
        if high_score == 0 or attempts_counter < high_score:
            high_score = attempts_counter
            print ("WAY TO GO! You just set a new high score")
        attempts_counter=1
        user_input=start_game()

print ("See you later, Have a nice day!!! ")

        




