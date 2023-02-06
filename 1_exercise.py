'''https://www.practicepython.org/exercise/2014/01/29/01-character-input.html'''

# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Note: for this exercise, the expectation is that you explicitly write out the year 
# (and therefore be out of date the next year). If you want to do this in a generic way,
# see exercise 39.

# Extras:

# 1. Add on to the previous program by asking the user for another number 
# and printing out that many copies of the previous message.
# (Hint: order of operations exists in Python)

# 2. Print out that many copies of the previous message on separate lines.
# (Hint: the string "\n" is the same as pressing the ENTER button)

YEAR = 2023

def int_getter(thing: str) -> int :
    while True :
        num = input(f'Please enter {thing}. >>> ')
        if not num.isdigit() or int(num) < 1 or int(num) > 99 :
            print('Please enter a number between 0 and 100!')
            continue
        break
    
    return int(num)

def main() -> None :
    print('This program will tell you in which year you will turn 100!')
    repeats = int_getter('how many repeats of the output you would like')
    name = input('What is your name? >>> ')
    age = int_getter('your age')
    print('--------------------------------------------------')
    
    year100 = YEAR + (100 - age)
    
    for _ in range(repeats) :
        print(f'{name}, You will be 100 in the year: {year100}.')
        print(f'If you haven\'t yet had your birthday this year,')
        print(f'you will turn 100 in {year100-1}')
        print('--------------------------------------------------')

if __name__ == '__main__' :

    main()


