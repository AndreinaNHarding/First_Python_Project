import random

LOWER_RANGE = 1
UPPER_RANGE = 10

def start_game():
    print("-"*110)
    print("\n Welcome to the Guessing A Number Game! \n")
    print("-"*110)
    return input("Enter a number between 1 and 10: ")

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
        if number > number_to_guess:
             print ("It is lower than {}".format(number))
        elif number > 0 and number < number_to_guess:
             print ("It is bigger than {}".format(number))
        user_input= input("try again: ")
        attempts_counter += 1
        number=is_a_number(user_input)
    print("you got it!!!! {} was the number!! you used {} attempt(s)".format(number, attempts_counter))
    game_continue= input("Do you want to play again? ")
    if game_continue == 'y':
        attempts_counter=1
        user_input=start_game()

print ("See you later, Have a nice day!!! ")

        




