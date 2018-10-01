# Server definitions
HOST = 'localhost'  # The server's hostname or IP address
SERVER_PORT = 6969  # The port used by the server
SUCCESS_RESPONSE = "200 OK"
FAIL_FORMAT_RESPONSE = "300 message format error"
FAIL_LOGIN_RESPONSE = "410 Wrong UserID or Password"
FAIL_AUTH_RESPONSE = "402 user not allowed to execute this command"
FAIL_NOUSER_RESPONSE = "401 you are not currently logged in. Log in first."
MESSAGE_SIZE = 4096  # message transmission size

# Command definitions
GET_MESSAGE = "MSGGET"
STORE_MESSAGE = "MSGSTORE"
ROOT_SHUTDOWN = "SHUTDOWN"
USER_LOGIN = "LOGIN"
USER_LOGOUT = "LOGOUT"
END_SESSION = "QUIT"
