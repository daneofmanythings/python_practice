'''Holds the game class'''

from player import RPSPlayer
from constants import THROW_DICT, Responses

class RPSGame:
    def __init__(self) :
        self.players:list[RPSPlayer] = list()
        self.rounds_played:int = 1
        self.playing:bool = True

    def add_player(self, player:RPSPlayer) -> None :
        '''Adds a player to the players list'''
        self.players.append(player)        
    
    def compare_throws(self) -> RPSPlayer | None :
        '''Returns the player that wins or None in the case of a tie
           after comparing throws from the class attribute'''
        result = THROW_DICT[self.players[0].current_throw][self.players[1].current_throw]
        self.rounds_played += 1          
        
        if result :
            self.players[0].has_won()
            return self.players[0]
        elif result is False :  # has to be False. Can't be None.
            self.players[1].has_won()
            return self.players[1]
        else :
            None

    def play_again(self, response: Responses) -> None:
        '''Adjusts the value of playing'''
        if response == Responses.NO :
            self.playing = False