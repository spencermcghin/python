import socket
import sys
import mimetypes
import os

def response_ok(body=b"this is a pretty minimal response", mimetype=b"text/plain"):
    """returns a basic HTTP response"""
    resp = []
    resp.append(b"HTTP/1.1 200 OK")
    resp.append(b"Content-Type: ", mimetype)
    resp.append(b"")
    resp.append(body)
    return b"\r\n".join(resp)

def response_method_not_allowed():
    """returns a 405 Method Not Allowed response"""
    resp = []
    resp.append("HTTP/1.1 405 Method Not Allowed")
    resp.append("")
    return "\r\n".join(resp).encode('utf8')

def response_not_found():
    """returns a 404 Not Found response"""
    resp = []
    resp.append("HTTP/1.1 404 Not Found")
    resp.append("")
    return "\r\n".join(resp).encode('utf8')

def parse_request(request):
    first_line = request.split("\r\n", 1)[0]
    method, uri, protocol = first_line.split()
    if method != "GET":
        raise NotImplementedError("We only accept GET")
    return uri

def resolve_uri(uri):
    """This method should return appropriate content and a mime type"""
    webroot = "webroot/"
    try:
        if os.path.isfile(webroot + uri):
            if uri.endswith('.py'):
                mime_type = b'text/x-python'
            else:
                mime_type = mimetypes.guess_type(webroot + uri)[0].encode('utf8')
            with open(webroot + uri, 'rb') as f:
                content = f.read()
        else:
            mime_type = b'text/plain'
            content = "\r\n".join(os.listdir(webroot + uri)).encode('utf8')

    except IOError:
        raise NameError("Resource does not exist")

    return content, mime_type

def server(log_buffer=sys.stderr):
    address = ('127.0.0.1', 10000)
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

if __name__ == '__main__':
    server()
    sys.exit(0)
