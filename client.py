import socket, sys, pickle
from card import Card

from player import Player

class Client:

    def __init__(self, name: str, playerID: int) -> None:
        self.player: Player = Player(name, playerID)    # client's state of player

    def send():
        pass

    # TODO: add parsing logic for msgs from server
    def receive():
        pass

# should turn this into a connectToServer() function which spawns a new thread for the connection
# also a sendToServer() and receiveFromServer() funcs, and constructor with Player obj for client
if __name__ == '__main__':

    HOST, PORT = "localhost", 8073
    print('Welcome to Love Letter!')
    clientName = input('Enter your name: ')

    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        
        # Connect to server
        sock.connect((HOST, PORT))

        sock.sendall(f'{clientName}\n'.encode('utf-8')) # send name to server
        sock.recv(1024)                                 # receive welcome from server with 
        
        print('waiting for game to start...')
        msg = sock.recv(1024)                                 # wait for game start msg from server
        print(msg.decode('utf-8'))

        card = sock.recv(1024)                                 # get drawn card from server
        unpickledCard = pickle.loads(card)
        print('You drew a', unpickledCard.name)


        # start of main event loop from client side
        while True:
            print('DEBUG in main event loop')
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
