import socket

serv_sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    proto = 0
)

port = 8073

serv_sock.bind(('127.0.0.1', port))
serv_sock.listen(5)
print('server listening on', port)

while True:
    # Accept new connections in an infinite loop.
    client_sock, client_addr = serv_sock.accept()
    print('New connection from', client_addr)

    chunks = []
    while True:
        
        # Keep reading while the client is writing.
        data = client_sock.recv(2048)
        if not data:
            # Client is done with sending.
            break
        chunks.append(data)

    client_sock.sendall(b''.join(chunks))
    client_sock.close()