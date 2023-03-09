
def seive_of_eratosthenes(upper_bound:int) -> list[int] :
    '''Uses the seive to generate a list of primes up to
    the upper bound'''

    nums = list(range(2, upper_bound + 1))
    for num in nums :
        multiple = num
        while multiple < upper_bound + 1 :
            multiple += num
            if multiple in nums :
                nums.remove(multiple)

    return nums
