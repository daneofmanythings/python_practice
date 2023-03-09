'''https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html'''

# Write a password generator in Python.
# Be creative with how you generate passwords - 
# strong passwords have a mix of lowercase letters, uppercase letters,
# numbers, and symbols. The passwords should be random, generating a new 
# password every time the user asks for a new password.
# Include your run-time code in a main method.

# Extra:

# Ask the user how strong they want their password to be.
# For weak passwords, pick a word or two from a list.

from string import ascii_letters, digits, punctuation
from random import choices

WEAK = ascii_letters
MEDIUM = WEAK + digits
STRONG = MEDIUM + punctuation

STRENGTH_DICT = {
    '1': WEAK,
    '2': MEDIUM,
    '3': STRONG
}

def generate_pw(characters: str, length: int) -> str :
    return ''.join(choices(characters, k=length))


def input_getter_strength() -> int :
    while True :
        response = input(f'>>> ')
        if response not in STRENGTH_DICT :
            continue
        return STRENGTH_DICT[response]

def input_getter_length() -> int :
    while True :
        response = input('>>>')
        if not response.isdigit() or int(response) < 1 :
            continue
        return int(response)

def input_getter_more() -> bool :
    while True :
        response = input(f'>>> ')
        if response not in ('y','n') :
            continue
        if response == 'y' :
            return True
        return False
    
def main() :
    print('Welcome to a password generator.')
    is_running = True
    while is_running :
        
        print('How string would you like your password?')
        print('1. Weak')    
        print('2. Medium')
        print('3. Strong')
        strength = input_getter_strength()
        
        print('How long would you like your password?', end='')
        length = input_getter_length()
        
        print(generate_pw(strength, length))
        
        print('Would you like to generate another password? (y/n)', end='')
        is_running = input_getter_more()
    print('l8r')

if __name__ == '__main__' :
    main()
