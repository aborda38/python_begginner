#Ask the user for a number. Depending on whether
#the number is even or odd, print out an appropriate
#message to the user.

def run():
    num_a = int(input("Type a number --> "))
    if num_a % 2 == 0:
        print("The number", num_a, "is even.")
        if num_a % 4 == 0:
            print("The number", num_a, "is a multiple of 4.")
    else:
        print("The number", num_a, "is odd.")
    num = int(input("Type a number to check --> "))    
    check = int(input("Type a number to divide by --> "))
    if num % check == 0:
        print("The number", num, "divides evenly by", check)   
    else:
        print("The number", num, " does not divide evenly by", check)

if __name__ == "__main__":
    run()
