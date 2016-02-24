#This is a simple server application used for connection over TCP sockets

import socket


def main():

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    host = socket.gethostname()

    s.bind((host,9000))
    s.listen(5)

    while True:
        clientsocket,addr = s.accept()
        print "Connection from ", addr
        clientsocket.send("Thank you for connecting..")
        clientsocket.close()

if __name__ == '__main__':
    main()