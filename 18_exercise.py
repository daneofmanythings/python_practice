'''https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html'''

# Create a program that will play the “cows and bulls” game with the user.
# The game works like this:

# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
# For every digit that the user guessed correctly in the correct place,
# they have a “cow”. For every digit the user guessed correctly in the wrong 
# place is a “bull.” Every time the user makes a guess, tell them how many 
# “cows” and “bulls” they have. Once the user guesses the correct number,
# the game is over. Keep track of the number of guesses the user makes 
# throughout teh game and tell the user at the end.

from string import digits
from random import choices

def input_getter_guess() -> int :
    '''Gets and validates input for this script'''
    while True :
        response = input('>>>')
        if not response.isdigit() or int(response) not in range(1000, 10000) :
            continue
        return response

def list_comparer(lst1:list, lst2:list) -> int :
    '''Counts the number of cows'''
    count = 0
    for x, y in zip(lst1, lst2) :
        if x == y :
            count += 1
    return count

def main() :
    target = choices(digits, k=4)
    target_as_str = ''.join(ele for ele in target)
    guess_counter = 0
    print('Guess a number between 1000 and 9999')
    
    while True :
        guess = list(input_getter_guess())
        guess_counter += 1
        cows = list_comparer(guess, target)
        if cows == 4 :
            print(f'Good job! The number was {target_as_str}')
            print(f'It took you {guess_counter} guesses.')
            break
        print(f'{cows} cows, {4-cows} bulls')

if __name__ == '__main__' :
    main()