#Marcel Champagne 52532335 and German Krikorian 81781612 Section 6 Assignment 2.

import socket
import collections

Connection = collections.namedtuple("Connection", "socket socket_input socket_output")

def make_connection(host: str, port: int) -> Connection:
    ''' Makes a new connection with in and out pseudo-files.'''
    new_socket = socket.socket()

    new_socket.connect((host,port))

    new_socket_in = new_socket.makefile('r')
    new_socket_out = new_socket.makefile('w')

    return Connection(new_socket, new_socket_in, new_socket_out)

def close_connection(connection: Connection) -> None:
    ''' Closes a connection and its input and output pseudo-files.'''
    connection.socket_input.close()
    connection.socket_output.close()
    connection.socket.close()

def send_message(connection: Connection, message: str) -> None:
    '''Sends a message with '\r\n' and flushes the output stream.'''
    connection.socket_output.write(message + '\r\n')
    connection.socket_output.flush()

def read_message(connection: Connection) -> str:
    '''Reads a message from the input stream and strips the last character.'''
    return connection.socket_input.readline()[:-1]

def start_game(connection: Connection) -> None:
    '''Sends a message to the server in order to start a new game.'''
    send_message(connection, "AI_GAME")

def login(connection: Connection, username: str) -> None:
    '''Sends a message to the server in order to login with a username.'''
    send_message(connection, "I32CFSP_HELLO "+username)

    
