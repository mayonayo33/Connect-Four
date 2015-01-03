#Marcel Champagne 52532335 and German Krikorian 81781612 Section 6 Assignment 2.

import connectfour_network
import connectfour_game
import connectfour

HOST = 'evil-monkey.ics.uci.edu'
PORT = 4444

def user_interface() -> None:
    ''' Displays a user interface which asks for a username and starts a new game.'''
    
    connection = connectfour_network.make_connection(HOST,PORT)

    username = get_username()

    try:

        connectfour_network.login(connection,username)
        print(connectfour_network.read_message(connection))
        connectfour_network.start_game(connection)
        print(connectfour_network.read_message(connection))
        run_game(connection)

    finally:
        
        connectfour_network.close_connection(connection)

def run_game(connection: connectfour_network.Connection) -> None:
    ''' Runs the main loop for the game, sending the user turn to the server and reading the AI move. Breaking when someone wins. '''

    game_state = connectfour.new_game_state()
    connectfour_game.display_board(game_state)

    while True:
        
        game_state = user_turn(connection, game_state)

        connectfour_game.display_board(game_state)

        server_message = connectfour_network.read_message(connection)
        
        if server_message == "OKAY":

            new_game_state = server_turn(connection, game_state)

            if game_state != new_game_state:
                game_state = new_game_state
            else:
                print("The server has not made a valid move, the connection will close.")
                break

            connectfour_game.display_board(game_state)

        elif server_message == "WINNER_RED":
            connectfour_game.game_over(connectfour.RED)
            break
        elif server_message == "WINNER_YELLOW":
            connectfour_game.game_over(connectfour.YELLOW)
            break
        else:
            print(server_message)

        server_message = connectfour_network.read_message(connection)
        
        if server_message == "READY":
            print("It is your turn again!")
            print()
        elif server_message == "WINNER_RED":
            connectfour_game.game_over(connectfour.RED)
            break
        elif server_message == "WINNER_YELLOW":
            connectfour_game.game_over(connectfour.YELLOW)
            break
        else:
            print(server_message)

def user_turn(connection:  connectfour_network.Connection, game_state: connectfour.ConnectFourGameState) -> None:
    ''' Gets input from the user and returns the game state'''
    move_column = connectfour_game.choose_column()
    move_type = connectfour_game.choose_move_type()
    
    game_state = connectfour_game.move(game_state, move_column, move_type)
    send_turn_to_server(connection, move_type, move_column)
    return game_state

def server_turn(connection:  connectfour_network.Connection, game_state: connectfour.ConnectFourGameState) -> None:
    ''' Reads the turn from the server AI and returns the game state. '''

    print()
    print("The AI is taking it's turn..")

    AI_move = connectfour_network.read_message(connection)
    AI_moves = AI_move.split()
    AI_move_type = AI_moves[0].lower()
    try:
        AI_column_number = int(AI_moves[1])
    except ValueError:
        return game_state   
    if AI_move_type in ['drop','pop'] and AI_column_number > 0 and AI_column_number < connectfour.BOARD_COLUMNS:
        game_state = connectfour_game.move(game_state,AI_column_number,AI_move_type)
        return game_state
    else:
        return game_state

def send_turn_to_server(connection:  connectfour_network.Connection, move_type: str, move_column: int) -> None:
    ''' Sends a turn to the server. '''
    connectfour_network.send_message(connection,move_type.upper()+" "+str(move_column))   

            


def get_username() -> str:
    ''' Asks the user to specify a username.'''
    while True:
        username = input("Please enter a username (no spaces):\n")
        username = username.strip()
        if ' ' not in username and len(username) > 0:
            break
        else:
            print("Invalid username, please try again.")
    return username

if __name__ == "__main__":
    user_interface()
