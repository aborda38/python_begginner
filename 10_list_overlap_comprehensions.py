#Take two lists, and write a program that returns a list that contains
#only the elements that are common between the lists (without duplicates).
#Make sure your program works on two lists of different sizes. 
#EXTRA: Randomly generate two lists to test this

import random
def run ():
    a = random.sample(range(1,21),15)
    b = random.sample(range(1,15),7)
    # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 12, 13]
    presolve = []

    for i in a:
        if i in b:
            presolve.append (i)
    print("List A --> ", a)
    print("List B --> ", b)
    solve = []

    for i in presolve:
        if i not in solve:
            solve.append (i)
    print("The common elements between List A and List B are --> ", solve)

if __name__ == '__main__':
    run()