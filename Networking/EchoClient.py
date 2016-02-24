# This is simple echo client which will be connect to a server and echo a message to recive it back in the loop

import socket

def main():
    s = socket.socket()
    host = socket.gethostname()
    port = 12345

    s.connect((host,port))
    s.sendall(b'Hello World')
    data = s.recv(1024)
    s.close()
    print str(data)
if __name__ == '__main__':
    main()