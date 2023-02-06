'''https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html'''

# Take two lists, say for example these two:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# and write a program that returns a list that contains only the elements that are common between the lists 
# (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:

# 1. Randomly generate two lists to test this
# 2. Write this in one line of Python (don’t worry if you can’t figure this out at this point 
#    -- we’ll get to it soon)

import random as ran

A = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def int_getter(thing: str) -> int :
    while True :
        num = input(f'Please enter {thing} >>> ')
        if not num.isdigit() :
            print('Please enter a number!')
            continue
        break
    
    return int(num)

class RandomList(list) :
    def __init__(self, low, high, length) :
        super().__init__()
        self.low = low
        self.high = high
        self.length = length

        for _ in range(length) :
            self.append(ran.randint(low, high))

def find_intersection(lst1:list[int], lst2:list[int]) -> list[int] :
    return list(set(lst1).intersection(set(lst2)))  # Single line, Extra #2

def selection_loop_for_rand_lists() -> list[RandomList[int]] :
    
    list_nums = ('1', '2')
    snippets = (
        'the lower bound for list',
        'the upper bound for list',
        'the length for list'
    )

    random_lists = []
    for str_num in list_nums :
        list_info = []
        for snippet in snippets :
            list_info.append(int_getter(snippet + ' ' + str_num))
        random_lists.append(RandomList(*list_info))
    
    return random_lists

def main() :
    # Main part
    # return find_intersection(A,B)

    # Extra #1
    return find_intersection(*selection_loop_for_rand_lists())

    # Extra #2
    # See above at find_intersection() definition

if __name__ == '__main__' :
    print(main())
