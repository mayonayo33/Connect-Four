#Marcel Champagne 52532335 and German Krikorian 81781612 Section 6 Assignment 2.

import connectfour

def display_board(game_state: connectfour.ConnectFourGameState) -> None:
    ''' Displays the game state in the console. '''
    print()
    for i in range(connectfour.BOARD_COLUMNS):
        print(i+1,end=' ')
    print()

    for i in range(connectfour.BOARD_ROWS):
        for j in range(connectfour.BOARD_COLUMNS):
            if game_state.board[j][i] == connectfour.NONE:
                print(". ", end = '')
            else:
                print(game_state.board[j][i]+" ", end = '')
        print()
    print()

def choose_column() -> int:
    ''' Asks the user to choose a column.'''
    while True:
        col = input("Select the column for your turn:\n")
        try:
            col = int(col)
        except:
            print("Invalid input, please enter a number.")
        else:
            if col > 0 and col <= connectfour.BOARD_COLUMNS:
                return col
            else:
                print("Invalid column, you must select a valid column.")

def choose_move_type() -> str:
    ''' Asks the user to choose a move type.'''
    while True:
        move_type = input("Would you like to 'drop' or 'pop'?\n")
        if move_type == 'drop' or move_type == 'pop':
            return move_type
        else:
            print("Invalid command, please enter 'drop' or 'pop'.")


def move(game_state: connectfour.ConnectFourGameState, column_number: int, move_type: str) -> None:
    '''Applies a move to the game state.'''
    
    try:
        if move_type == 'drop':
            return connectfour.drop_piece(game_state,column_number-1)
        elif move_type == 'pop':
            return connectfour.pop_piece(game_state,column_number-1)
    except connectfour.InvalidConnectFourMoveError:
        print("Invalid move.")
        return game_state
    except connectfour.ConnectFourGameOverError:
        print("The game is already over!")
        return game_state

def game_over(player: str) -> None:
    '''Checks if a player has won.'''
    if player == connectfour.RED:
        print("Red has won, the game is now over.")
    elif player == connectfour.YELLOW:
        print("Yellow has won, the game is now over.")
