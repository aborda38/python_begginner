#Ask the user for a number and determine whether the number is prime or not.
        
def run ():
    def numprime():
        user_number = int(input('Type a number to check primality --> '))
        contador = 0
        for i in range (1, user_number + 1):
            if user_number % i == 0:
                contador = contador + 1
  
        if contador == 2:
            print ("***", user_number, "--> is a prime number, XD")
        else:
            print ("***", user_number, "--> isn't a prime number, :(")
    #Function end.

    numprime()

if __name__ == '__main__':
    run()