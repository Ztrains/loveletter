import socket
import sys

HOST, PORT = "localhost", 8073
clientName = input('Enter your name: ')
# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))

    #sock.recv(128)                              # receive welcome from server
    #clientName = input('Enter your name: ')    # input name for game
    sock.sendall(f'{clientName}\n'.encode('utf-8'))    # send name to server
    #print('DEBUG sent name', clientName, 'to server')
    sock.recv(1024)                              # receive 2nd welcome from server with name
    #print('DEBUG after 2nd recv')

    # start of main event loop from client side
    while True:
        #print('DEBUG in main event loop')
        line = sys.stdin.readline()
        if not line:
            # end of stdin, exit whole script
            break
        sock.sendall(f'{line}'.encode('utf-8'))
        while True:
            data = sock.recv(128)
            print(data.decode('utf-8'), end='')
            if len(data) < 128:
                # no more of this message, go back to waiting for next message
                break
