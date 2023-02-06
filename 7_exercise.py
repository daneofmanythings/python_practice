'''https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html'''

# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and makes a new list 
# that has only the even elements of this list in it.

A = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def list_evener(lst: list[int]) -> list[int] :
    return [num for num in lst if num % 2 == 0]

def main() :
    return list_evener(A)

if __name__ == '__main__' :
    print(main())