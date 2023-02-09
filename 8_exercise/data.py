'''Holds the constants'''

from enum import Enum, auto

COMPUTER = 'computer'

class Throws(Enum) :  # Values are strings to aid with printing. strEnum isn't implemented in 3.10
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSORS = 'scissors'

# Currently, YES is never used
class Responses(Enum) :
    YES = auto()
    NO = auto()

THROW_CONVERTER = {  # Implementation specific
    'r': Throws.ROCK,
    'p': Throws.PAPER,
    's': Throws.SCISSORS
}

RESPONSE_CONVERTER = {
    'y': Responses.YES,
    'n': Responses.NO
}

THROW_DICT = {  # Nested dictionary to grab the winner.
    Throws.ROCK: {
        Throws.ROCK: None,
        Throws.PAPER: False,
        Throws.SCISSORS: True
    },
    Throws.PAPER: {
        Throws.ROCK: True,
        Throws.PAPER: None,
        Throws.SCISSORS: False
    },
    Throws.SCISSORS: {
        Throws.ROCK: False,
        Throws.PAPER: True,
        Throws.SCISSORS: None
    }
}

# HELPER FUNCTIONS
def data_input(string:str) -> str :
    return input(string)

def first_in_str_validator(string:str, conversion_dict:dict[str:Enum]) -> tuple[bool,Enum]:
    '''Validates the string against the conversion dictionary and returns the converted
       object if True'''
    if not string or string[0] not in conversion_dict :
        return False, None
    return True, conversion_dict[string[0]]

def str_validator(string:str, target:str) -> bool :
    return string.lower() == target