#Create a program that asks the user to enter
#their name and their age. Print out a message 
#addressed to them that tells them the year that
#they will turn 100 years old.

#datetime. Work through the time
import datetime
def run():
    user_name = input("Type your name --> ")
    user_age = int(input("Type your current age --> "))

    year = datetime.datetime.now()
    current_year =  year.strftime ("%Y")
    current_year = int(current_year)
    when_age_100 = (100 - user_age) + current_year

    print("Mr or Ms", user_name, "in the year", when_age_100, "you will be 100 years old. Do exercise and eat well. :)")


if __name__ == '__main__':
    run()