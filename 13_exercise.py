'''https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html'''

# Write a program that asks the user how many Fibonnaci numbers to generate 
# and then generates them. Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.

# --- Implementing a memoization decorator for recursive fibonacci function ---

from typing import Callable

def memoize(cache_max:int=128) -> Callable:  # Parameterizing the decorator
    def outer(func:Callable) -> Callable :  # memoization decorator
        from functools import wraps

        cache = dict()

        @wraps(func)
        def inner(*args, **kwargs) :  # This returns whatever func returns
            arguements = str(args) + str(kwargs)  # Unique signature per input
            if arguements not in cache :
                cache[arguements] = func(*args, **kwargs)
            # Restricting the size of the cache
            if len(cache) > cache_max :
                variable = enumerate(cache)  # used to isolate the first entry in cache
                _, key = next(variable)
                del cache[key]
            return cache[arguements] 
        
        return inner
    return outer

@memoize(3)
def fib_recursive(n:int) -> int :
    return 1 if n < 3 else fib_recursive(n-1) + fib_recursive(n-2)
    
print(fib_recursive(20))
