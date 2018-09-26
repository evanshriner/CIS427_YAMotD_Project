import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def server_loop():
    while True:
        conn, addr = server.accept()
        print('got connection from: ' + addr[0])
        while True:
            got = conn.recv(4096)
            if got == "QUIT":
                conn.close()
            print(got)


if __name__ == "__main__":
    server.bind(('localhost', 6969))
    server.listen(5)
    server_loop()
