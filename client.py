#!/usr/bin/python

import socket
import constants

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def session_loop():
    session = True  # client wants to maintain session
    while session:
        input_command = raw_input()
        command_tokens = input_command.split()
        if command_tokens[0] == constants.GET_MESSAGE:
            client.sendall(constants.GET_MESSAGE)
            data = client.recv(4096)

        elif command_tokens[0] == constants.STORE_MESSAGE:
            client.sendall(constants.STORE_MESSAGE)

        elif command_tokens[0] == constants.ROOT_SHUTDOWN:
            client.sendall(constants.ROOT_SHUTDOWN)

        elif command_tokens[0] == constants.USER_LOGIN:
            client.sendall(constants.USER_LOGIN)

        elif command_tokens[0] == constants.USER_LOGOUT:
            client.sendall(constants.USER_LOGOUT)

        elif input_command[0] == constants.END_SESSION:
            session = False

        else:
            print("Did not recognize command. please try again")


if __name__ == "__main__":
    client.connect((constants.HOST, constants.SERVER_PORT))
    print("Connected to server. Enter a command...")
    session_loop()
    print("Ending session...")
