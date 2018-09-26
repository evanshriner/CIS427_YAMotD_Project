import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


if __name__ == "__main__":
    client.connect(('localhost', 6969))
