import socket

# Create client socket.
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 8073
# Connect to server (replace 127.0.0.1 with the real server IP).
client_sock.connect(('127.0.0.1', port))

# Send some data to server.
client_sock.sendall(b'Hello, world')
client_sock.shutdown(socket.SHUT_WR)

# Receive some data back.
chunks = []
while True:
    data = client_sock.recv(2048)
    if not data:
        break
    chunks.append(data.decode())
print('Received', repr(''.join(chunks)))

# Disconnect from server.
client_sock.close()