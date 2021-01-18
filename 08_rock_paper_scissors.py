def run():
    response = "Y"
    response = response.lower()
    while response == "y":
        print("Choose --> Rock = 1; Paper = 2; Scissors = 3;" )
        election_gamer_1 = int(input("Gamer #1 --> "))
        while election_gamer_1 < 0 or election_gamer_1 > 3:
            election_gamer_1 = int(input("Gamer #1 --> "))
        
        election_gamer_2 = int(input("Gamer #2 --> "))
        while election_gamer_2 < 0 or election_gamer_2 > 3:
            election_gamer_2 = int(input("Gamer #2 --> "))
            
        if election_gamer_1 == election_gamer_2:
            print ("It's a tie!")
        elif (election_gamer_1 == 1 and election_gamer_2 == 3) or (election_gamer_1 == 2 and election_gamer_2 == 1) or (election_gamer_1 == 3 and election_gamer_2 == 2):
            print("WINNER: GAMER 1")
        else:
            print("WINNER: GAMER 2")
        response = str(input("Will we continue play, now? [Y/N] --> "))
        response = response.lower()   
    else:
        print("Bye, bye!!!")
if __name__ == '__main__':
    run()