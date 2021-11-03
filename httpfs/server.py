import socket
import threading

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


def handle_Request(connInput, addrInput):
    conn = connInput
    addr = addrInput
    print(f'NEW CONNECTION: {addr}connected')
    # connected = True
    # conn.send('Zoo wee mama').encode(FORMAT)
    # while connected:
    #     msg_length= int(conn.recv(HEADER).decode(FORMAT))
    #     msg = conn.recv(msg_length).decode(FORMAT)
    #     print(f'{addr} says : {msg}')
    #     connected = False
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
