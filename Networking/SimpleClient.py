# This is a simple client application used to connect and recieve date from server using socket TCP

import socket

def main():

    #Create socket object, if you ignore argument by default TCP domain socket gets created
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #get the local host name using socket function
    host = socket.gethostname()

    #connect to the server using host addr and port
    s.connect((host,9000))

    # Receive data from the server
    print s.recv(1024)
    s.close()

if __name__ == '__main__':
    main()