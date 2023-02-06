'''https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html'''

# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# 1. If the number is a multiple of 4, print out a different message.
# 2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


def int_getter(thing: str) -> int :
    while True :
        num = input(f'Please enter {thing}. >>> ')
        if not num.isdigit() :
            print('Please enter a number!')
            continue
        break
    
    return int(num)

def main() :
    print('This program will tell you if a number divides another!')

    dividend = int_getter('the dividend')
    divisor = int_getter('the divisor')

    if not dividend % divisor :
        print(f'{divisor} evenly divides {dividend}!')
    else :
        print(f'{divisor} does not evenly divide {dividend}!')

if __name__ == '__main__' :
    main()