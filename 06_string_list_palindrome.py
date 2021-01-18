#Ask the user for a string and print
#out whether this string is a palindrome or not.

def run():
    print("**************************************************************")
    print("SEARCHING PALINDROMES")
    print("NOTE: Don't put apostrophes or tildes if you write in spanish.")
    print("**************************************************************")
    frase = str(input("Type a frase or word to analyse --> "))
    frase = frase.lower()
    a = []
    for i in frase:
        if i != ' ':
            a.append(i)
    
    a_reverse = a[::-1]
    
    if a == a_reverse:
        print(frase, 'is a palindrome! Cool XD')
    else:
        print(frase, "isn't a palindrome! Cool :(")

if __name__ == '__main__':
    run()