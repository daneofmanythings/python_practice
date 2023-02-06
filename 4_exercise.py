'''https://www.practicepython.org/exercise/2014/02/26/04-divisors.html'''

# Create a program that asks the user for a number and then prints out a 
# list of all the divisors of that number. (If you don’t know what a divisor is,
# it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 
# 26 / 13 has no remainder.)

def int_getter(thing: str) -> int :
    while True :
        num = input(f'Please enter {thing}. >>> ')
        if not num.isdigit() :
            print('Please enter a number!')
            continue
        break
    
    return int(num)

def main() :
    num = int_getter('the number to find the divisors for')

    for i in range(2, num + 1 // 2) :
        if not num % i :
            print (i)


if __name__ == '__main__' :
    main()