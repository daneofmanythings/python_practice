'''https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html'''

# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to help you. 
# Take this opportunity to practice using functions, described below.

# --- Implementing the Sieve of Eratosthenese ---

NUMBER = 259  # Number to check for primality


def seive_of_eratosthenes(upper_bound:int) -> list[int] :
    nums = list(range(2, upper_bound + 1))
    for num in nums :
        multiple = num
        while multiple < upper_bound + 1 :
            multiple += num
            if multiple in nums :
                nums.remove(multiple)

    return nums

print(NUMBER in seive_of_eratosthenes(NUMBER))