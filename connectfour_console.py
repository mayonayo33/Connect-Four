#Marcel Champagne 52532335 and German Krikorian 81781612 Section 6 Assignment 2.

import connectfour
import connectfour_game

def display_interface() -> None:
    ''' Displays the user interface which asks the user if they want to start a game.'''
    _welcome_message()

    while True:
        choice = input("Would you like to start a new game? (Y/N)\n")
        if choice.lower() == 'y':
            _game()
        elif choice.lower() == 'n':
            break
        else:
            print("Invalid choice, please enter 'Y' or 'N'")


def _game() -> None:
    '''Runs the main game loop in which two players alternate taking turns.'''
    game_state = connectfour.new_game_state()

    while True:
        connectfour_game.display_board(game_state)

        if _turn(game_state) == connectfour.RED:
            print("It is Red Player's turn.")
        elif _turn(game_state) == connectfour.YELLOW:
            print("It is Yellow Player's turn.")
        print()

        column_number = connectfour_game.choose_column()
        move_type = connectfour_game.choose_move_type()
        game_state = connectfour_game.move(game_state,column_number,move_type)
        winning_player = connectfour.winning_player(game_state)

        if winning_player != connectfour.NONE:
            connectfour_game.game_over(winning_player)
            connectfour_game.display_board(game_state)
            break
    
def _turn(game_state: connectfour.ConnectFourGameState) -> str:
    ''' Returns the current turn of a game state.'''
    return game_state.turn

def _welcome_message() -> None:
    ''' Displays the welcome message.'''
    print("Welcome to connect four!")

if __name__ == "__main__":
    display_interface()
