import socket
import threading

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


def handle_Request(connInput, addrInput):
    conn = connInput
    addr = addrInput
    print(f'NEW CONNECTION: {addr}connected')
    connected = True
    from_client = ''
    while connected:
        data = conn.recv(4096)
        if not data: break
        from_client += data.decode(FORMAT)
        print ("FROM CLIENT: \n"+from_client)
        headers = from_client.split('\r\n', 1)
        request_type = headers[0].split(' /',1)
        # print(headers[0])
        # print(request_type[0])
        headers = headers[0]
        request_type = request_type[0]
        if request_type=='GET':
            print("Received GET request")
        elif request_type == 'POST':
            print("Received POST request")
        else:
            print("Request type not supported at this time")
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
