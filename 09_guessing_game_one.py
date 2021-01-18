#Generate a random number between 1 and 9
#(including 1 and 9). Ask the user to guess the
# number, then tell them whether they guessed too
# low, too high, or exactly right.

#I generate a random number between 1 and 100.

import random

def run():

    pc_number = random.randint(1,101)
    user_name = int(input("Give a number --> "))

    while user_name != pc_number:
        if user_name < pc_number:
            print ("Your number is too low!")
            user_name = int(input("Give me other number --> "))
            
        elif user_name > pc_number:
            print ("Your number is too high!")
            user_name = int(input("Give me other number --> "))
            
    else:
        print("You WINS")


if __name__=='__main__':
    run()