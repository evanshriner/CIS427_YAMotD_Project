#!/usr/bin/python

import socket
import sys
import constants

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
users = {'root': 'root01', 'john': 'john01', 'david': 'david01', 'mary': 'mary01'}


def server_loop():
    on = True
    while on:
        print("waiting for input")
        # get command
        got = conn.recv(constants.MESSAGE_SIZE)
        # parse command
        tokens = got.split()
        if tokens:
            print("Client said: " + got)
            # if requesting message
            if tokens[0] == constants.GET_MESSAGE:
                conn.send(constants.SUCCESS_RESPONSE + "\n" + next_message())
            # if posting message
            elif tokens[0] == constants.STORE_MESSAGE:
                # if logged in
                if get_user():
                    conn.send(constants.SUCCESS_RESPONSE)
                    m = conn.recv(constants.MESSAGE_SIZE) + "\n"
                    print("storing message: " + m)
                    msg_list.append(m)
                    conn.send(constants.SUCCESS_RESPONSE)
                else:
                    conn.send(constants.FAIL_NOUSER_RESPONSE)
            # if trying to login
            elif tokens[0] == constants.USER_LOGIN:
                # if proper username password combination
                if len(tokens) == 3:
                    if users[tokens[1]] == tokens[2]:
                        conn.send(constants.SUCCESS_RESPONSE)
                        # set current user
                        set_user(tokens[1])
                        print("logged on: " + tokens[1])
                    else:
                        conn.send(constants.FAIL_LOGIN_RESPONSE)
                else:
                    conn.send(constants.FAIL_FORMAT_RESPONSE)
            # if trying to logout
            elif tokens[0] == constants.USER_LOGOUT:
                # if a user is logged in
                if get_user():
                    print("logged off:" + get_user())
                    set_user(None)
                    conn.send(constants.SUCCESS_RESPONSE)
                else:
                    conn.send(constants.FAIL_LOGIN_RESPONSE)
            # if trying to end session
            elif tokens[0] == constants.END_SESSION:
                conn.send(constants.SUCCESS_RESPONSE)
                # clear user
                set_user(None)
                # wait for next connection
                await_connection()
            # if trying to root shutdown
            elif tokens[0] == constants.ROOT_SHUTDOWN:
                # if root logged in
                if get_user() == "root":
                    conn.send(constants.SUCCESS_RESPONSE)
                    on = False
                else:
                    conn.send(constants.FAIL_AUTH_RESPONSE)
            # if command not found
            else:
                conn.send(constants.FAIL_FORMAT_RESPONSE)


def set_user(username):
    global user
    user = username


def get_user():
    if 'user' in globals():
        return user
    else:
        return None


# increment through list of messages
def next_message():
    global msg_index
    if msg_index == len(msg_list):
        msg_index = 0

    m = msg_list[msg_index]
    msg_index += 1
    return m


def await_connection():
    global conn, addr
    print ("awaiting connection...")
    conn, addr = server.accept()
    print('got connection from: ' + addr[0])


if __name__ == "__main__":
    try:
        server.bind((constants.HOST, constants.SERVER_PORT))
    except socket.error, msg:
        print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

    try:
        f = open('messages.txt')
    except IOError:
        print "Could not open list of messages."
        sys.exit()

    # read file into list
    msg_list = f.readlines()
    msg_index = 0
    # only allow one connection
    server.listen(2)
    await_connection()

    server_loop()

    conn.shutdown(socket.SHUT_RDWR)
    conn.close()

    # write appended messages to file
    try:
        f = open('messages.txt', 'w+')
    except IOError:
        print "Could not open list of messages. Messages were not written."
        sys.exit()

    for message in msg_list:
        f.write(message)

    print("Server shutting down...")
    sys.exit()
