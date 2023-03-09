'''https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html'''

# This week’s exercise is going to be revisiting an old exercise (see Exercise 5),
# except require the solution in a different way.

# Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# and write a program that returns a list that contains only the elements that 
# are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
# Write this in one line of Python using at least one list comprehension.

import random

class RandomList(list) :
    def __init__(self, low, high, length) :
        super().__init__()
        self.low = low
        self.high = high
        self.length = length

        for _ in range(length) :
            self.append(random.randint(low, high))

c = RandomList(0, 1000, random.randint(1,1000))
d = RandomList(0, 1000, random.randint(1,1000))

result = [ele for ele in c if ele in d]  # K.
print(sorted(result))