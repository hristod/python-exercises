'''
Create a program that asks the user to enter their name and
their age. Print out a message addressed to them that tells
them the year that they will turn 100 years old.
'''


def main():
    age = input("Tell me your age:")
    age = int(age)
    years_to_hundred = int(100 - age)
    print("You will be 100 in %d years!" % years_to_hundred)

main()