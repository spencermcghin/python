import socket
import sys

# Create the basic socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Connect socket to server listening port
address = ('127.0.0.1', 10000)
print(sys.stderr, 'Connecting to %s port %s' % address)
server_socket.bind(address)


# Connect and send data
try:

    message = 'This will be repeated over and over again.'
    print(sys.stderr, 'Sending %s' % message)
    server_socket.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = server_socket.recv(16)
        amount_received += len(data)
        print(sys.stderr, 'received "%s"' % data)

finally:
    print(sys.stderr, 'Socket closing.')
    server_socket.close()