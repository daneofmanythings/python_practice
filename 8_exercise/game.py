'''Holds the game class'''

from player import RPSPlayer
from constants import THROW_DICT, CONTINUE_RESPONSES

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
        result = THROW_DICT[self.players[0].current_throw[0]][self.players[1].current_throw[0]]
        self.rounds_played += 1          
        
        if result :
            self.players[0].has_won()
            return self.players[0]
        elif result is False :  # has to be False. Can't be None.
            self.players[1].has_won()
            return self.players[1]
        else :
            None

    def play_again(self, response: str) -> bool | None :
        '''Validates a response and updates the self.playing boolean. Returns true for
           while loop shenanigans'''
        if response.lower()[0] not in CONTINUE_RESPONSES:
            return True
        
        if response == CONTINUE_RESPONSES[1] :
            self.playing = False