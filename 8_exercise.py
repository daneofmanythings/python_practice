'''https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html'''

# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner,
# and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock
# ---------------------------------------------------------------------------------------

#########################################################################################
# The goal of this is to build an app where the game logic is separate from the display #
# logic. This is a learning experience and will likely be very suboptimal. All of the   #
# string objects and print logic should only be in global variables and a class.        #
#########################################################################################

import os
import random

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

class RPSPlayer :
    def __init__(self, name, is_computer=False) :
        self.name = name 
        self.current_throw = None
        self.wins:int = 0
        self._is_computer = is_computer

    def has_won(self) :
        '''Increments wins'''
        self.wins += 1

    def get_throw(self, throw: str) :
        '''Validates and updates a throw string. Returns true for
           while loop shenanigans.'''
        if throw.lower()[0] not in THROW_DICT :
            return True
        else :
            self.current_throw = throw.lower()

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

    def get_throw(self) :
        '''Computer chooses a throw randomly'''
        self.current_throw = random.choice(tuple(THROW_DICT))

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

    def string_inserter(self, str_idx_list:list[list[str:int]], into:str) -> str :
        '''Allows you to insert multiple strings into a target string
           by giving it a list of pairs: (string_to_be_inserted, index_to_insert)
           Returns the string'''
        for thing in str_idx_list :
            string, idx = thing  # for readability
            into = into[:idx] + str(string) + into[idx:]
        return into

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
    
    # TODO: THIS MIGHT BE TOTALLY GARBAGE. NOT HANDLED WELL!?
    def redraw(self) :
        '''Redraws the screen to avoid clutter and keep secrets'''
        try :
            os.system('clear')
        except :
            os.system('cls')
        self.cli_print(self.opener)

def main() -> None :
    '''The game logic. Lots of loops.'''
    printer = RPSCLIPrinter()
    printer.redraw()
    printer.cli_print(printer.single_player)
    
    game = RPSGame()
    
    # Getting the names of the players
    for num in range(NUM_PLAYERS) :  
        player_name = input(  # The indenting is to make nested func calls easier to read
            printer.string_inserter(
            ((str(num + 1), -5),), printer.player_prompt))
        
        if player_name.lower() == COMPUTER :  # Checking for an AI opponent
            game.add_player(RPSComputer(player_name + str(num)))
        else :
            game.add_player(RPSPlayer(player_name))
        
        printer.redraw()
    
    # Main play loop
    while game.playing :
        
        # Retrieving and storing the throws for both players
        for player in game.players :
            if player._is_computer :
                player.get_throw()
            else :
                while player.get_throw(  # Nested function calls split up for readability
                    input(
                    printer.string_inserter(
                    ((player.name, 0),), printer.get_throw))) :

                    continue  # This might be hacky logic
        
        # Comparing the throws to find the round winner
        round_winner = game.compare_throws()
        if round_winner is None :
            printer.cli_print(printer.declare_tie)
        else :
            # Checking to see if there's a computer to print its throw
            for player in game.players :
                if player._is_computer :
                    printer.cli_print(
                        printer.computer_throw_stringer(player)  # Custom method for pretty printing
                    )  
            # Printing the winner
            printer.cli_print(
                printer.round_winner_stringer(round_winner)  # Custom method for a pretty printing
            )
        
        # Ask to play again
        while game.play_again(input(printer.play_again)):
            continue  # Hacky?
        
        printer.redraw()
    
    # Once the game ends, find winner, print winner
    winner, loser = max(game.players), min(game.players)

    if winner.wins == loser.wins :
        printer.cli_print(printer.declare_tie)
    else :
        printer.cli_print(
            printer.game_winner_stringer(winner, loser)  # Custom method for pretty printing
        )
    
    # Buh Bye
    printer.cli_print(printer.closer)

if __name__ == '__main__' :
    main()
