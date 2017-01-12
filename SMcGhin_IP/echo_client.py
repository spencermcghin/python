import socket
import sys

# Create the basic socket
local_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Connect socket to server listening port
local_address = ('127.0.0.1', 10000)
print(sys.stderr, 'Connecting to %s port %s' % local_address)
local_socket.bind(local_address)

