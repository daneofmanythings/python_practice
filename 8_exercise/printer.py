'''Holds the printer class'''

import os
from player import RPSPlayer, RPSComputer
from constants import THROW_CONVERTER

class RPSCLIPrinter :
    def __init__(self) :
        self.opener = ''' 
            ----------------------------------------------------\n
            Welcome to a friendly game of Rock, Paper, Scissors\n
                 Try not to peek at your opponent\'s moves!\n
            ----------------------------------------------------
            '''
        self.single_player = '''If you would like to play against the computer enter \'computer\' as the name.\n'''
        self.closer = '''
            \n\t    ====================================================\n
            \t\t  Thank you for playing!
        '''
        self.player_prompt = 'Enter the name for player  >>> '
        self.get_throw = ', choose rock, paper, or scissors >>> '
        self.computer_throw = ' threw  '
        self.play_again = 'Would you like to play again? (y or n) >>> '
        self.round = '\n--------------------- Round  ----------------------'
        self.tie_round = 'The game is a tie.'
        self.win_round = ' has won with ! They have won  times.'
        self.declare_tie = 'The game is a tie.'
        self.declare_winner = '\n is the winner! They won  to  '

    def string_inserter(self, str_idx_list:list[list[str:int]], target:str) -> str :
        '''Allows you to insert multiple strings into a target string
           by giving it a list of pairs: (string_to_be_inserted, index_to_insert)
           Returns the string'''
        for str_idx in str_idx_list :
            string, idx = str_idx  # for readability
            target= target[:idx] + str(string) + target[idx:]
        return target 

    def round_winner_stringer(self, player:RPSPlayer) -> str:
        '''Method that implements the inserter for a specific task
           Returns a string for the round winner'''
        str_idx_list = (
            (THROW_CONVERTER[player.current_throw[0]], 14),
            (player.wins, -7),
            (player.name, 0)
        )
        return self.string_inserter(str_idx_list, self.win_round)
    
    def game_winner_stringer(self, winner:RPSPlayer, loser:RPSPlayer) -> str :
        '''Method that implements the inserter for a specific task
           Returns a string for the game winner'''
        str_idx_list = (
            (winner.name, 1),
            (winner.wins, -5),
            (loser.wins, -1)
        )
        return self.string_inserter(str_idx_list, self.declare_winner)
    
    def computer_throw_stringer(self, computer:RPSComputer) -> str:
        '''Method that implements the inserter for a specific task
           Returns what the AI threw'''
        str_idx_list = (
            (computer.name, 0),
            (THROW_CONVERTER[computer.current_throw], -1)
        )
        return self.string_inserter(str_idx_list, self.computer_throw)
    
    def cli_print(self, string: str) -> None :
        '''Keeping print calls out of other classes/functions'''
        print(string)

    def cli_input(self, string:str) -> str :
        return input(string)
    
    def cli_input_with_inserter(self, str_idx_list:list[list[str:int]], target:str) -> str :
        '''Implementing inputs with string inserter to reduce line bloat in main()
           and to pull out implementation details'''
        return input(self.string_inserter(str_idx_list, target))
    
    def redraw(self) :
        '''Redraws the screen to avoid clutter and keep secrets'''
        if os.name == 'nt' :
            os.system('cls')
        else :
            os.system('clear')
        self.cli_print(self.opener)