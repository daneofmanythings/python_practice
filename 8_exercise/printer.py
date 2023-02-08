'''Holds the printer class'''

import os
from player import RPSPlayer

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
        self.player_prompt = 'Enter the name for player {0} >>> '
        self.get_throw = '{0}, choose rock, paper, or scissors >>> '
        self.computer_throw = '{0} threw {1}'
        self.play_again = 'Would you like to play again? (y or n) >>> '
        self.round = '\n--------------------- Round  ----------------------'
        self.win_round = '{0} has won with {1}! They have won {2} times.'
        self.declare_tie = 'The game is a tie.'
        self.declare_winner = '\n{0} is the winner! They won {1} to {2}'

    def formatter(self, strings:tuple[str], target:str) -> str :
        return target.format(*strings)

    def round_winner_stringer(self, player:RPSPlayer) -> str:
        '''Method that implements the formatter for a specific task
           Returns a string for the round winner'''
        str_list = (
            player.name,
            player.current_throw.value,
            player.wins,
        )
        return self.formatter(str_list, self.win_round)
    
    def game_winner_stringer(self, winner:RPSPlayer, loser:RPSPlayer) -> str :
        '''Method that implements the formatter for a specific task
           Returns a string for the game winner'''
        str_list = (
            winner.name,
            winner.wins,
            loser.wins
        )
        return self.formatter(str_list, self.declare_winner)
    
    def throw_stringer(self, player:RPSPlayer) -> str:
        '''Method that implements the formatter for a specific task
           Returns what the AI threw'''
        str_list = (
            player.name,
            player.current_throw.value
        )
        return self.formatter(str_list, self.computer_throw)
    
    def cli_print(self, string: str) -> None :
        '''Keeping print calls out of other classes/functions'''
        print(string)

    def cli_input(self, string:str) -> str :
        return input(string)
    
    def redraw(self) :
        '''Redraws the screen to avoid clutter and keep secrets'''
        if os.name == 'nt' :
            os.system('cls')
        else :
            os.system('clear')
        self.cli_print(self.opener)