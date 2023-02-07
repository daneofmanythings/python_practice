'''Holds the constants'''

THROW_DICT = {  # Nested dictionary to grab the winner.
    'r': {
        'r': None,
        'p': False,
        's': True
    },
    'p': {
        'r': True,
        'p': None,
        's': False
    },
    's': {
        'r': False,
        'p': True,
        's': None
    }
}

THROW_CONVERTER = {  # Exists for prettier printing.
    'r': 'rock',
    'p': 'paper',
    's': 'scissors'
}

# Adding simple global constants to make the code look cleaner.
NUM_PLAYERS = 2
CONTINUE_RESPONSES = 'y', 'n'
COMPUTER = 'computer'