def happy_numbers(upper_bound:int) -> list[int] :
    '''Returns a list of happy numbers up to the upper bound'''
    
    happy_nums:list[int] = list()

    for num in range(upper_bound) :
        if is_happy(num) :
            happy_nums.append(num)

    return happy_nums


def is_happy(num:int) -> bool :
    '''Returns whether or not a number is happy'''

    seen:set[int] = set()

    while num != 1 :
        num = digit_add(num)

        if num in seen :
            return False
        
        seen.add(num)
    
    return True


def digit_add(num:int) -> int :
    '''Sums the digits of an integer and returns the sum'''

    digit_sum = 0
    
    while num >= 1 :
        num, remainder = divmod(num, 10)
        digit_sum += remainder ** 2

#    print(digit_sum)
    return digit_sum


if __name__ == "__main__":
#    print(digit_add(926))
#    print(is_happy(911))
    print(happy_numbers(100))
