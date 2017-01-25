import socket
import sys


def client(msg):
    server_address = ('localhost', 50000)
    sock = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP
    )
    print(
        'connecting to {0} port {1}'.format(*server_address),
        file=sys.stderr
    )
    sock.connect(server_address)
    response = ''
    done = False
    bufsize = 1024
    try:
        print('sending "{0}"'.format(msg), file=sys.stderr)
        sock.sendall(msg.encode('utf8'))
        while not done:
            chunk = sock.recv(bufsize)
            if len(chunk) < bufsize:
                done = True
            response += chunk.decode('utf8')
        print('received "{0}"'.format(response), file=sys.stderr)
    finally:
        print('closing socket', file=sys.stderr)
        sock.close()
    return response


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usg = '\nusage: python echo_client.py "this is my message"\n'
        print(usg, file=sys.stderr)
        sys.exit(1)

    msg = sys.argv[1]
    client(msg)
