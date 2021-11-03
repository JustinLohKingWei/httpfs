import socket
import threading
import os

HEADER = 64
FORMAT = 'utf-8'


def do_Get(connInput, request):
    files = os.listdir('data')
    code = "200 OK"
    body = ""
    query = request.split('/', 1)
    query = query[1]
    if query == "":
        for f in files:
            print(f)
            body += f
            body += "\n"
    else:
        body += "Some file content"
        body += "\n"
        #implement GET /foo

    response = "HTTP/1.1 "+code+"\n"+"Content-Type: text/html\n"+"\n"
    response += body+"\n"
    connInput.send(response.encode(FORMAT))


def do_Post(connInput, request):
    files = os.listdir('/data')
    code = "200 OK"
    body = ""
    #implement POST /foo
    response = "HTTP/1.1 "+code+"\n"+"Content-Type: text/html\n"+"\n"
    response += body+"\n"
    connInput.send(response.encode(FORMAT))


def handle_Request(connInput, addrInput):
    conn = connInput
    addr = addrInput
    print(f'NEW CONNECTION: {addr}connected')
    connected = True
    from_client = ''
    while connected:
        data = conn.recv(4096)
        if not data:
            break
        from_client += data.decode(FORMAT)
        print("FROM CLIENT: \n"+from_client+"\n")
        headers = from_client.split('\r\n', 1)
        request = headers[0].split('HTTP/1.', 1)
        request_type = headers[0].split(' /', 1)
        headers = headers[0]
        request = request[0]
        request_type = request_type[0]
        if request_type == 'GET':
            print("Received GET request")
            do_Get(conn, request)
        elif request_type == 'POST':
            print("Received POST request")
            do_Post(conn, request)
        else:
            print("Request type is not supported at this time")
            print(request)
        connected = False

    conn.close()
    print('Connection closed')


def start(serverInput, serveraddr):
    server = serverInput
    server.listen()
    print(f"Server is listening on {serveraddr}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_Request, args=(conn, addr))
        thread.start()
        print(f"ACTIVE CONNECTIONS : {threading.active_count()-1}")


def server(portInput):
    PORT = portInput
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = ('', PORT)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    print(f"{SERVER} server starting at port {PORT} ")
    start(server, SERVER)
