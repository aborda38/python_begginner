#Write one line of Python that takes this list a 
#and makes a new list that has only the even 
#elements of this list in it.

import random

def run():
    a = random.sample(range(1, 300), 13)
    # a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    c=[i for i in a if i % 2 == 0]; print("Random list -->", a); print("List of even elements -->", c)

if __name__ == '__main__':
    run()