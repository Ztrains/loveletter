import socket
import sys

HOST, PORT = "localhost", 8073

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    while True:
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
