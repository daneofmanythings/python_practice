'''https://www.practicepython.org/exercise/2014/11/11/20-element-search.html'''

# Write a function that takes an ordered list of numbers 
# (a list where the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list and returns 
# (then prints) an appropriate boolean.

# Extras:

# Use binary search.

LIST = [1,3,4,5,6,7,8,9]
NUM = 10

def is_element_in_list(lst:list[int], ele:int) -> bool :
    return ele in lst

def binary_search(lst:list[int], ele:int) -> bool :
    mid = len(lst) // 2

    if lst[mid] == ele :
        return True
    if len(lst) == 1 :
        return False

    if lst[mid] < ele :
        return binary_search(lst[mid+1:], ele)    
    else :
        return binary_search(lst[:mid], ele)
    

print(binary_search(LIST, NUM))