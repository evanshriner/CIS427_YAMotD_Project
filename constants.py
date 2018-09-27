# Server definitions
HOST = 'localhost'  # The server's hostname or IP address
SERVER_PORT = 6969  # The port used by the server
SUCCESS_RESPONSE = "200 OK"
FAIL_RESPONSE = "300 message format error"
MESSAGE_SIZE = 4096  # message transmission size

# Command definitions
GET_MESSAGE = "MSGGET"
STORE_MESSAGE = "MSGSTORE"
ROOT_SHUTDOWN = "SHUTDOWN"
USER_LOGIN = "LOGIN"
USER_LOGOUT = "LOGOUT"
END_SESSION = "QUIT"
