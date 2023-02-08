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

from constants import (RESPONSE_CONVERTER, THROW_CONVERTER, computer_validator,
                       validator)
from game import RPSGame
from player import RPSComputer, RPSHuman
from printer import RPSCLIPrinter


def main() -> None :
    '''The game logic. Lots of loops.'''
    printer = RPSCLIPrinter()
    printer.redraw()
    printer.cli_print(printer.single_player)
    
    game = RPSGame()
    
    # Getting the names of the players
    for num in range(2) :  
        player_name = printer.cli_input(
            printer.formatter([num + 1], printer.player_prompt))
        
        if computer_validator(player_name) :  # Checking for an AI opponent
            game.add_player(RPSComputer(player_name + str(num)))
        else :
            game.add_player(RPSHuman(player_name))
        
        printer.redraw()
    
    # Main play loop
    while game.playing :
        
        # Retrieving and storing the throws for both players
        for player in game.players :
            if isinstance(player, RPSComputer) :
                player.set_throw()
            else :
                while True :  # This loop exists to validate input then convert input to enum
                    response = printer.cli_input(printer.formatter([player.name], printer.get_throw))
                    valid, converted = validator(response, THROW_CONVERTER)
                    
                    if not valid :
                        continue
                    
                    player.set_throw(converted)
                    break
        
        # Comparing the throws to find the round winner
        round_winner = game.compare_throws()
        printer.redraw()
        
        # Printing the throws
        for player in game.players :
            printer.cli_print(printer.throw_stringer(player))
        
        # Printing the winner or tie
        if round_winner is None :
            printer.cli_print(printer.declare_tie)
        else :
            printer.cli_print(printer.round_winner_stringer(round_winner))
        
        # Ask to play again
        while True :
            valid, converted = validator(
                printer.cli_input(printer.play_again), RESPONSE_CONVERTER)
            
            if not valid :
                continue
            
            game.play_again(converted)
            break
        
        printer.redraw()
    
    # Once the game ends, find winner, print winner
    winner, loser = max(game.players), min(game.players)

    if winner.wins == loser.wins :
        printer.cli_print(printer.declare_tie)
    else :
        printer.cli_print(printer.game_winner_stringer(winner, loser))
    
    # Buh Bye
    printer.cli_print(printer.closer)

if __name__ == '__main__' :
    main()
