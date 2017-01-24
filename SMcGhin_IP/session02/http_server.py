import socket
import sys
import os
import magic


def server(log_buffer=sys.stderr):
    address = ('127.0.0.1', 50000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("making a server on {0}:{1}".format(*address), file=log_buffer)
    sock.bind(address)
    sock.listen(1)

    try:
        while True:
            print('waiting for a connection', file=log_buffer)
            conn, addr = sock.accept()  # blocking
            try:
                print('connection - {0}:{1}'.format(*addr), file=log_buffer)
                request = ''
                while True:
                    data = conn.recv(1024)
                    request += data.decode('utf8')
                    if len(data) < 1024:
                        break
                try:
                    uri = parse_request(request)
                except NotImplementedError:
                    response = response_method_not_allowed()
                else:
                    try:
                        content, mime_type = resolve_uri(uri)
                    except NameError:
                        response = response_not_found()
                    else:
                        response = response_ok(content, mime_type)

                print('sending response', file=log_buffer)
                conn.sendall(response)
            finally:
                conn.close()

    except KeyboardInterrupt:
        sock.close()
        return


def response_ok(content, mime_type):
    """returns a basic HTTP response"""
    resp = list()
    resp.append(b'HTTP/1.1 200 OK')
    resp.append(b'Content-Type: text/plain')
    resp.append(b'')
    resp.append(content)
    resp.append(mime_type)
    return b'\r\n'.join(resp)


def parse_request(request):
    first_line = request.split('\r\n', 1)[0]
    method, uri, protocol = first_line.split()
    if method != 'GET':
        raise NotImplementedError('This only accepts GET')
    print(sys.stderr, 'Request is ok.')
    return uri


def response_method_not_allowed():
    """returns a 405 Method Not Allowed response"""
    resp = list()
    resp.append(b"HTTP/1.1 405 Method Not Allowed")
    resp.append(b"")
    return b"\r\n".join(resp)


def response_not_found():
    """returns a 404 Not Found Error"""
    resp = list()
    resp.append(b"HTTP/1.1 404 Not Found")
    resp.append(b"")
    return b"\r\n".join(resp)


def resolve_uri(uri):
    server_path = os.getcwd() + uri
    mime_type = magic.from_file(server_path, mime=True)  # identify mimetype
    content = list()
    try:
        if os.path.isfile(server_path):
            file_content = open(server_path).read(), mime_type
            content.append(b'Content-Type: text/plain')
            content.append(b'')
            content.append(file_content)
        elif os.path.isdir(server_path):
            dir_content = os.listdir(server_path), mime_type
            content.append(b'Content-Type: text/plain')
            content.append(b'')
            content.append(dir_content)

    except NameError:
        print(response_not_found())

    return content, mime_type


if __name__ == '__main__':
    server()
    sys.exit(0)
