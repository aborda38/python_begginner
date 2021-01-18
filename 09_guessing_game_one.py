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