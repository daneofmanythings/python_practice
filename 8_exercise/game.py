'''Holds the game class'''

from player import RPSPlayer
from data import THROW_DICT, Responses

class RPSGame:
    def __init__(self) :
        self.players:list[RPSPlayer] = list()
        self.round_num:int = 1
        self.playing:bool = True

    def add_player(self, player:RPSPlayer) -> None :
        '''Adds a player to the players list'''
        self.players.append(player)        
    
    def round_played(self) -> None :
        '''Increments round_num property'''
        self.round_num += 1
    
    #TODO: Maybe change how this functions and throw some of this logic to the main function
    def compare_throws(self) -> RPSPlayer | None :
        '''Returns the player that wins or None in the case of a tie
           after comparing throws from the class attribute'''
        result = THROW_DICT[self.players[0].current_throw][self.players[1].current_throw]
        
        if result :
            self.players[0].has_won()
            return self.players[0]
        elif result is False :  # has to be False. Can't be None.
            self.players[1].has_won()
            return self.players[1]
        else :
            None

    def reset_throws(self) -> None :
        '''Resets the current_throw property for players.'''
        for player in self.players :
            player.set_throw(None)

    def play_again(self, response: Responses) -> None:
        '''Adjusts the value of playing'''
        if response == Responses.NO :
            self.playing = False
