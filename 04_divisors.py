#Create a program that asks the user for a number
#and then prints out a list of all the divisors of 
#that number.

def run():
    numa = int(input('Type a number --> '))
    lista = []
    for i in range (1, numa+1):
        if numa % i == 0:
            lista.append(i)
    
    print("The divisors of", numa, "are", lista)


if __name__ == '__main__':
    run()