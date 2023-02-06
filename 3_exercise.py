'''https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html'''

# Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# Extras:
# 1. Instead of printing the elements one by one, make a new list that has all the elements 
#    less than 5 from this list in it and print out this new list.
# 2. Write this in one line of Python.
# 3. Ask the user for a number and return a list that contains only elements from 
#    the original list a that are smaller than that number given by the user.

A = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def int_getter(thing: str) -> int :
    while True :
        num = input(f'Please enter {thing}. >>> ')
        if not num.isdigit() :
            print('Please enter a number!')
            continue
        break
    
    return int(num)

def one_line(lst: list[int], bound:int=5) -> list[int] :
    return [i for i in lst if i < bound]  # <- Single line, Extra 2

def main() :
    
    # Main part
    # for i in one_line(A):
        # print(i)

    # Extra 1
    # print(one_line(A))

    # Extra 2
    # See above to one_line()

    # Extra 3
    upper_bound = int_getter('an upper bound')    
    print(one_line(A, upper_bound))

if __name__ == '__main__' :
    main()