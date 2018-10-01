this project contains a client and server socket communication line. for the program to work properly,
the server must be started first. when the client connects, both the client and server will acknowledge
this connection. they will both be placed in their respective loops for standard operation. the basic structure
for the client is to send a command and wait for the servers response. if it was a successful message, the server
will tell the client, and the client will follow up accordingly.

other than the main loop, the client has the following implemented:
success(res) # this function is a simplified way to determine if the response was OK.
post(input) # this function sends the message to the server and intercepts its response.


other than the main loop, the server has the following implemented:
set_user(username) # sets the current user on the server
get_user() # gets the current user on the server (if initalized)
next_message() # increments and returns the next message in the message list
await_connection() # waits for the next person to connect to the server

no known bugs

sample outputs:
C: MSGGET
S: 200 OK
Alphabet ‘O’ stands for ‘OPPORTUNITY’ which is absent in YESTERDAY, Available Once in T’O’DAY, & Available Thrice in T’O’M’O’RR’O’W. Never lose hope.

C: MSGSTORE
S: 200 OK
C: Imagination is more important than knowledge. S: 200 OK

C:  SHUTDOWN
S:  200 OK

C: LOGIN root root01
S: 200 OK