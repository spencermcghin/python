import socket
import sys

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Bind socket to port
address = ('127.0.0.1', 10000)
print(sys.stderr, 'Server starting on %s, port %s' % address)
server_socket.bind(address)

# Listen for client connections
server_socket.listen(1)

while True:
    print('Waiting for a client connection')
    connection, local_address = server_socket.accept()

    try:
        print(sys.stderr, 'Received connection from', local_address)

        while True:
            data = connection.recv(32)
            print(sys.stderr, 'Received %s' % data)
            if data:
                print(sys.stderr, 'Sending back to client.')
                connection.sendall(data)
            else:
                print(sys.stderr, 'Sorry, no more data from', local_address)
                break
    finally:
        connection.close()
