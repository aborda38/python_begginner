#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the
# number, then tell them whether they guessed too low, too high, or exactly right.

#I generate a random number between 1 and 100.

#EXTRAS: 1. Keep the game going until the user types “exit”
#EXTRAS: 2. Keep track of how many guesses the user has taken, and when the game ends, print this out.
import random

def run():
    print ("****************")
    print ("GUESS THE NUMBER")
    print ("****************")
    pc_number = random.randint(1,101)
    user_name = int(input("Give me a number --> "))
    count = 1

    while (user_name != pc_number):
        if user_name < pc_number:
            print ("Your number is too low!")
            user_opinion = str(input("Type exit to stop the game to continue type enter --> "))
            if user_opinion == "exit":
                break
            else: 
                user_name = int(input("Give me other number --> "))
            
        elif user_name > pc_number:
            print ("Your number is too high!")
            user_opinion = str(input("Type exit to stop the game to continue type enter --> "))
            if user_opinion == "exit":
                break
            else:
                user_name = int(input("Give me other number --> "))
        count += 1    
    else:
        print("Chances -->", count, "[You WINS] XD XD XD")


if __name__=='__main__':
    run()