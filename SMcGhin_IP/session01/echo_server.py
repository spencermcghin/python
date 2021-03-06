import socket
import sys


def server(log_buffer=sys.stderr):
    # set an address for our server
    address = ('127.0.0.1', 50000)
    # Replace the following line with your code which will instantiate
    #       a TCP socket with IPv4 Addressing, call the socket you make 'sock'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # You may find that if you repeatedly run the server script it fails,
    #       claiming that the port is already used.  You can set an option on
    #       your socket that will fix this problem. We DID NOT talk about this
    #       in class. Find the correct option by reading the very end of the
    #       socket library documentation:
    #       http://docs.python.org/3/library/socket.html#example
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(address)
    # log that we are building a server
    print("making a server on {0}:{1}".format(*address), file=log_buffer)

    # bind your new sock 'sock' to the address above and begin to listen
    #       for incoming connections
    sock.listen(1)

    try:
        # the outer loop controls the creation of new connection sockets. The
        # server will handle each incoming connection one at a time.
        while True:
            print('waiting for a connection', file=log_buffer)

            # make a new socket when a client connects, call it 'conn',
            #       at the same time you should be able to get the address of
            #       the client so we can report it below.  Replace the
            #       following line with your code. It is only here to prevent
            #       syntax errors
            connection, client_address = sock.accept()
            try:
                print('connection - {}'.format(client_address), file=log_buffer)

                # the inner loop will receive messages sent by the client in
                # buffers.  When a complete message has been received, the
                # loop will exit
                while True:
                    # receive 16 bytes of data from the client. Store
                    #       the data you receive as 'data'.  Replace the
                    #       following line with your code.  It's only here as
                    #       a placeholder to prevent an error in string
                    #       formatting
                    data = connection.recv(16)
                    print('received "{0}"'.format(data.decode('utf8')))
                    # Send the data you received back to the client, log
                    # the fact using the print statement here.  It will help in
                    # debugging problems.
                    if data:
                        print('sent "{0}"'.format(data.decode('utf8')))
                        connection.sendall(data)
                    else:
                        print('no more data from', client_address)
                        break
                    # TODO: Check here to see if the message you've received is
                    # complete.  If it is, break out of this inner loop.

            finally:
                # When the inner loop exits, this 'finally' clause will
                #       be hit. Use that opportunity to close the socket you
                #       created above when a client connected.
                print('echo complete, client connection closed', file=log_buffer)
                connection.close()

    except KeyboardInterrupt:
        # Use the python KeyboardInterrupt exception as a signal to
        #       close the server socket and exit from the server function.
        #       Replace the call to `pass` below, which is only there to
        #       prevent syntax problems
        sock.close()
        print('quitting echo server', file=log_buffer)


if __name__ == '__main__':
    server()
    sys.exit(0)

