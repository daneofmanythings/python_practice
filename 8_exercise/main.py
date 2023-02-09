"""https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html"""

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

from data import (
    COMPUTER,
    RESPONSE_CONVERTER,
    data_input,
    str_validator,
    first_in_str_validator,
)
from game import RPSGame
from player import IOPlayer, AIPlayer
from printer import RPSCLIPrinter


def main() -> None:
    """The game logic. Lots of loops."""
    printer = RPSCLIPrinter()
    printer.redraw()
    printer.cli_print(printer.single_player)

    game = RPSGame()

    # Getting the names of the players
    for num in range(2):  # <- Will always be 2 for this implementation
        player_name = data_input(
            printer.formatter([num + 1], printer.player_prompt))

        if str_validator(player_name, COMPUTER):  # Checking for an AI opponent
            game.add_player(AIPlayer(player_name + str(num)))
        else:
            if not player_name :
                game.add_player(IOPlayer('dumb' * (num + 1)))
            else :
                game.add_player(IOPlayer(player_name))

        printer.redraw()

    printer.cli_print(printer.formatter([game.round_num], printer.round))

    # Main play loop
    while game.playing:
        # Getting and setting the throws for both players
        for player in game.players:
            throw = player.get_throw()
            player.set_throw(throw)

            printer.redraw()
            printer.cli_print(printer.formatter([game.round_num], printer.round))

        # Comparing the throws to find the round winner
        round_winner = game.compare_throws()

        # Printing the throws
        for player in game.players:
            printer.cli_print(printer.throw_stringer(player))

        # Printing the winner or tie
        if round_winner is None:
            printer.cli_print(printer.declare_tie)
        else:
            printer.cli_print(printer.round_winner_stringer(round_winner))

        # Ask to play again
        while True:
            response = data_input(printer.play_again)

            if not first_in_str_validator(response, RESPONSE_CONVERTER):
                continue

            game.play_again(RESPONSE_CONVERTER[response])
            break

        # End of round cleanup. Resetting throws and incrementing the round number.
        game.reset_throws()
        game.round_played()

        printer.redraw()
        printer.cli_print(printer.formatter([game.round_num], printer.round))

    printer.redraw()

    # Once the game ends, find winner, print winner
    winner, loser = max(game.players), min(game.players)

    if winner.wins == loser.wins:
        printer.cli_print(printer.declare_tie)
    else:
        printer.cli_print(printer.game_winner_stringer(winner, loser, game))

    # Buh Bye
    printer.cli_print(printer.closer)


if __name__ == "__main__":
    main()
