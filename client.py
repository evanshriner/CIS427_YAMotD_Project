#!/usr/bin/python

import socket
import sys
import constants

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def session_loop():
    session = True  # client wants to maintain session
    while session:
        # get input from user console
        input_command = raw_input()
        # send input to server
        response = post(input_command)
        # if server accepts command
        if success(response):
            # print response
            print(response)
            # check if 'set message' command entered
            command_tokens = input_command.split()
            if command_tokens[0] == constants.STORE_MESSAGE:
                # get message from user
                input_message = raw_input()
                #  print response from input message
                print (post(input_message))
            # check if quit command entered
            elif command_tokens[0] == constants.END_SESSION:
                session = False
            elif command_tokens[0] == constants.ROOT_SHUTDOWN:
                return True
        else:
            print(response)  # print the received error
    return False


def success(res):
    return_tokens = res.split()
    if return_tokens[0] == "200":
        return True
    else:
        return False


def post(input):
    # send command on the socket connection, return response
    client.sendall(input)
    return client.recv(constants.MESSAGE_SIZE)


if __name__ == "__main__":
    # connect to host and port of server
    try:
        client.connect((constants.HOST, constants.SERVER_PORT))
    except socket.error, msg:
        print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

    print("Connected to server. Enter a command...")
    # start session loop
    if not session_loop():
        # client quit, close connection
        client.shutdown(socket.SHUT_RDWR)
        client.close()
    print("Ending session...")
