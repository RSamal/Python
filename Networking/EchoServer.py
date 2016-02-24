# This is simple TCP socket server that echo backs the data client send

import socket

def main():

    serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    host = socket.gethostname()
    port = 12345
    serverSocket.bind((host,port))

    serverSocket.listen(1)
    conn,addr = serverSocket.accept()
    print "(connected by :", addr, ") "
    while True:
        data = conn.recv(1024)
        if not data : break
        conn.sendall(data)
        conn.close()

if __name__ == '__main__':
    main()