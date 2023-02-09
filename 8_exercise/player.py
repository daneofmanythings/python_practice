'''Holds the player class'''

from __future__ import annotations
import random
from data import Throws, THROW_DICT
from abc import ABC, abstractmethod

class RPSPlayer(ABC) :
    def __init__(self, name) :
        self.name = name
    
    @abstractmethod
    def has_won(self):
        pass

    @abstractmethod
    def get_throw(self):
        pass

    @abstractmethod
    def set_throw(self):
        pass

class RPSHuman(RPSPlayer) :
    def __init__(self, name) :
        self.name:str = name 
        self.current_throw:Throws = None
        self.wins:int = 0

    def has_won(self) -> None:
        '''Increments wins'''
        self.wins += 1

    def set_throw(self, throw:Throws | None) -> None :
        '''Sets the throw attribute'''
        self.current_throw = throw

    def get_throw(self) -> None :
        pass
    
    def __lt__(self, other:RPSPlayer) -> bool :
        return self.wins < other.wins
    
    def __str__(self) -> str :
        return self.name

    def __repr__(self) :
        return f'RPSHuman({self.name})'
    
class RPSComputer(RPSPlayer) :
    def __init__(self, name) :
        self.name:str = name
        self.current_throw:Throws = None
        self.wins:int = 0

    def has_won(self) -> None :
        '''Increments wins'''
        self.wins += 1

    def set_throw(self, throw:Throws | None) -> None :
        self.throw = throw

    def get_throw(self) -> None :
        '''Computer chooses a throw randomly'''
        self.current_throw = random.choice(tuple(THROW_DICT.keys()))

    def __lt__(self, other:RPSPlayer) -> bool :
        return self.wins < other.wins
    
    def __str__(self) -> str :
        return self.name

    def __repr__(self) -> str :
        return f'RPSComputer({self.name})'