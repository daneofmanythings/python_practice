'''Holds the printer class'''

import os
from player import RPSPlayer
from game import RPSGame

class RPSCLIPrinter :
    def __init__(self) :
        self.opener = ''' 
            ----------------------------------------------------\n
            Welcome to a friendly game of Rock, Paper, Scissors\n
                 Try not to peek at your opponent\'s moves!\n
            ----------------------------------------------------
            '''
        self.single_player = colored(255, 0, 0,
            '''If you would like to play against the computer enter \'computer\' as the name.\n'''
        )
        self.closer = '''
            \n\t    ====================================================\n
            \t\t  Thank you for playing!
        '''
        self.player_prompt = 'Enter the name for player {0} >>> '
        self.throw_prompt = '{0}, choose rock, paper, or scissors >>> '
        self.throw_output = '{0} threw {1}'
        self.play_again = '\nWould you like to play again? (y or n) >>> '
        self.round = colored(25, 100, 200,
            '\t\t\t\t  Round {0}\n')
        self.win_round = colored(0, 255, 0,
            '\n{0} has won with {1}! They have won {2} times.')
        self.declare_tie = 'The game is a tie.'
        self.declare_winner = '\n{0} is the winner! They won {1} to {2} out of {3} rounds.'

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
    
    def game_winner_stringer(self, winner:RPSPlayer, loser:RPSPlayer, game:RPSGame) -> str :
        '''Method that implements the formatter for a specific task
           Returns a string for the game winner'''
        str_list = (
            winner.name,
            winner.wins,
            loser.wins,
            game.round_num
        )
        return self.formatter(str_list, self.declare_winner)
    
    def throw_stringer(self, player:RPSPlayer) -> str:
        '''Method that implements the formatter for a specific task
           Returns what the AI threw'''
        str_list = (
            player.name,
            player.current_throw.value
        )
        return self.formatter(str_list, self.throw_output)
    
    def cli_print(self, string:str, **kwargs) -> None :
        '''Keeping print calls out of other classes/functions'''
        print(string, **kwargs)

    def redraw(self) :
        '''Redraws the screen to avoid clutter and keep secrets'''
        if os.name == 'nt' :
            os.system('cls')
        else :
            os.system('clear')
        self.cli_print(self.opener)
    
    def redraw_with_round_num(self, game:RPSGame) :
        '''Cleans up main() slightly'''
        self.redraw()
        self.cli_print(self.formatter([game.round_num], self.round))

# HELPER FUNCTION
def colored(r:int, g:int, b:int, text:str) -> str :
    '''Sets a string to a color specified by RGB values'''
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"