#Take a list, say for example this one:
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the
#elements of the list that are less than 5.

def run():
    a = [1, 1, 2, 3, 4, 5, 8, 13, 21, 3, 55, 89]
    b = []
    c = input("Type a number -->")
    c = int(c)
    for i in a:
        if i < c:
            print (i)
            b.append(i)
        else:
            pass
    print(b)


if __name__ == '__main__':
    run()