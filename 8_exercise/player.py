'''Holds the player class'''

from __future__ import annotations
import random
from data import Throws, THROW_CONVERTER, THROW_DICT, data_input, first_in_str_validator
from abc import ABC, abstractmethod

class RPSPlayer(ABC) :
    def __init__(self, name) :
        self.name = name
    
    @abstractmethod
    def has_won(self) -> None :
        pass

    @abstractmethod
    def get_throw(self) -> Throws :
        pass

    @abstractmethod
    def set_throw(self, throw:Throws) -> None :
        pass

class IOPlayer(RPSPlayer) :
    def __init__(self, name) :
        self.name:str = name 
        self.current_throw:Throws = None
        self.wins:int = 0

    def has_won(self) -> None:
        '''Increments wins'''
        self.wins += 1

    def get_throw(self) -> Throws :
        '''Implemented as a wrapper for helper functions from data module'''
        while True :
            response = data_input()

            if not first_in_str_validator(response, THROW_CONVERTER) :
                continue

            return THROW_CONVERTER[response]

    def set_throw(self, throw:Throws) -> None :
        '''Sets the throw attribute'''
        self.current_throw = throw

    def __lt__(self, other:RPSPlayer) -> bool :
        return self.wins < other.wins
    
    def __str__(self) -> str :
        return self.name

    def __repr__(self) :
        return f'RPSHuman({self.name})'
    
class AIPlayer(RPSPlayer) :
    def __init__(self, name) :
        self.name:str = name
        self.current_throw:Throws = None
        self.wins:int = 0

    def has_won(self) -> None :
        '''Increments wins'''
        self.wins += 1
    
    def get_throw(self) -> Throws :
        '''Computer chooses a throw randomly'''
        return random.choice(tuple(THROW_DICT.keys()))

    def set_throw(self, throw:Throws) -> None :
        '''Sets the throw attribute'''
        self.current_throw = throw

    def __lt__(self, other:RPSPlayer) -> bool :
        return self.wins < other.wins
    
    def __str__(self) -> str :
        return self.name

    def __repr__(self) -> str :
        return f'RPSComputer({self.name})'