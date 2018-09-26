import socket

HOST = 'localhost'  # The server's hostname or IP address
PORT = 6969        # The port used by the server

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if __name__ == "__main__":

    client.connect((HOST, PORT))
    client.sendall(b'Hello, world')
    data = client.recv(1024)

print('Received', repr(data))

