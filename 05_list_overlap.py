#Take two lists, and write a program that returns
#a list that contains only the elements that are
#common between the lists (without duplicates)


import random

def run ():
    #Random list range(1,whatever), num elements)
    aa = random.sample(range(1,150),13)
    bb = random.sample(range(1,150),21)
    # aa = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    # bb = [1, 1, 3, 4, 5, 6, 7, 8, 122, 10, 11, 12, 13]
    cc = []
    for i in bb:
        if i in aa:
            cc.append(i)
    
    solve = []

    for i in cc:
        if i not in solve:
            solve.append (i)

    #without duplicates
    
    
    print(aa)
    print(bb)
    print()
    print("The common elements are -->", solve)
if __name__ == '__main__':
    run()