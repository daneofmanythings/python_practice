'''https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html'''

# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

from random import randint

the_target = randint(1,9)

def input_getter(thing: str) -> int :
    while True :
        num = input(f'Please enter {thing}. >>> ')
        if num == 'exit' :
            return num
        if not num.isdigit() :
            print('Please enter a number or \'exit\'.')
            continue
        break
    
    return int(num)

num_guesses = 0
while True :
    guess = input_getter('a guess between 1 and 9')
    num_guesses += 1
    if guess == 'exit' :
        break
    elif guess > the_target :
        print(f'Too high!')
        continue
    elif guess < the_target :
        print(f'Too low!')
        continue
    else :
        print(f'You win! the number was {the_target}. It took you {num_guesses} guesses.')
        break
