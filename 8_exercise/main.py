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

from player import RPSPlayer, RPSComputer
from game import RPSGame
from printer import RPSCLIPrinter
from constants import NUM_PLAYERS, COMPUTER

def main() -> None :
    '''The game logic. Lots of loops.'''
    printer = RPSCLIPrinter()
    printer.redraw()
    printer.cli_print(printer.single_player)
    
    game = RPSGame()
    
    # Getting the names of the players
    for num in range(NUM_PLAYERS) :  
        player_name = printer.cli_input_with_inserter(
            ((str(num + 1), -5),), printer.player_prompt)
        
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
                    printer.cli_input_with_inserter(
                    ((player.name, 0),), printer.get_throw)
                ) :
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
        while game.play_again(printer.cli_input(printer.play_again)) :
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
