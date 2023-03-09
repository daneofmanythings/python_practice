'''https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html'''

# Write a program (function!) that takes a list and 
# returns a new list that contains all the elements of 
# the first list minus all the duplicates.

# Extras:

# 1. Write two different functions to do this - one 
# using a loop and constructing a list, and another using sets.
# 2. Go back and do Exercise 5 using sets, and write the 
# solution for that in a different function.

INPUT_LIST = [1,2,3,4,5,6,7,7,8]

def loop_(lst:list) -> list :
    new_lst = list()

    while lst :
        popped = lst.pop(0)
        if popped in lst :
            continue
        else :
            new_lst.append(popped)
    
    return new_lst

def set_(lst:list) -> list :
    return set(lst)

print(loop_(INPUT_LIST))