#!/usr/bin/python

import socket
import sys
import constants

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def server_loop():
    conn, addr = server.accept()
    print('got connection from: ' + addr[0])
    while True:
        got = conn.recv(4096)
        if got != "":
            print(got)
        if got == "SHUTDOWN":
            conn.send(constants.SUCCESS_RESPONSE)
            conn.close()


if __name__ == "__main__":
    # TODO: read messages file and put all into a global list
    try:
        server.bind((constants.HOST, constants.SERVER_PORT))
    except socket.error, msg:
        print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()
    server.listen(5)
    server_loop()
