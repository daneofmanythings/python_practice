'''Holds the player class'''

import random
from constants import Throws, THROW_DICT

class RPSPlayer :
    def __init__(self, name, is_computer=False) :
        self.name:str = name 
        self.current_throw:Throws = None
        self.wins:int = 0
        self._is_computer:bool = is_computer

    def has_won(self) -> None:
        '''Increments wins'''
        self.wins += 1

    def get_throw(self, throw:Throws) -> None :
        '''Validates and updates a throw string. Returns true for
           while loop shenanigans.'''
        self.current_throw = throw

    def __eq__(self, other) :
        '''Enables ordering'''
        return self.wins == other.wins
        
    def __lt__(self, other) :
        '''Enables ordering'''
        return self.wins < other.wins
    
    def __repr__(self) :
        '''Shouldn't need this, but I couldn't find a print bug,
           so I strong-armed it'''
        return self.name
    
class RPSComputer(RPSPlayer) :
    def __init__(self, name, is_computer=True) :
        super().__init__(self)
        self.name = name
        self._is_computer = is_computer

    def get_throw(self) -> None :
        '''Computer chooses a throw randomly'''
        self.current_throw = random.choice(tuple(THROW_DICT.keys()))
        