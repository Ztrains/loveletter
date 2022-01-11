import socket, sys, pickle, time, json
from typing import Dict
from card import Card

from player import Player

class Client:

    def __init__(self, name: str) -> None:
        self.player: Player = Player(name)    # client's state of player

    def printHand(self) -> None:
        print('Enter 1 or 2 for which card you wish to play from your hand:')
        for idx, card in enumerate(self.player.hand, start=1):  # print player's cards with idx starting at 1
            print(f'({idx}) {card.name} - {card.power}')

    def send():
        pass

    # TODO: add parsing logic for msgs from server
    def receive():
        pass

# TODO: refactor almost all of this below to use functions and be much cleaner
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
        
        client = Client(clientName)

        print('waiting for game to start...')
        while True:
            msg = sock.recv(1024)                       # wait for game start msg from server
            decodedMsg = msg.decode('utf-8')
            print('msg:', decodedMsg)
            if decodedMsg == 'Game started':
                break
            time.sleep(1)

        card = sock.recv(1024)                          # get drawn card from server
        unpickledCard: Card = pickle.loads(card)
        client.player.addCardToHand(unpickledCard)
        print('You drew a', unpickledCard.name)


        # start of main event loop from client side
        while True:
            print('DEBUG in main event loop')

            msg = sock.recv(1024)                       # should get 'Your turn' here if blocking
            decodedMsg = msg.decode('utf-8')
            print('DEBUG msg:', decodedMsg)

            card = sock.recv(1024)                          # get drawn card from server
            unpickledCard: Card = pickle.loads(card)
            client.player.addCardToHand(unpickledCard)
            print('You drew a', unpickledCard.name)

            client.printHand()


            line = None
            while True:
                line = sys.stdin.readline().strip()
                if line == '1' or line == '2':
                    # TODO need to add check if card played needs a target player sent as well
                    print('DEBUG valid input found')
                    break
                else:
                    print('Invalid input, enter 1 or 2')
            
            print('DEBUG before json serialization')

            # TODO: actually fill out target var
            target = 'bob'
            cardIndex = int(line) - 1
            dictToSend: Dict[str, str] = {'cardName': client.player.hand[cardIndex].name, 'target': target}
            encodedJson = json.dumps(dictToSend)

            if not line:
                # end of stdin, exit whole script
                break
            
            # TODO convert choice to json and send it
            print('DEBUG before sock.sendall with JSON')
            sock.sendall(f'{encodedJson}\n'.encode('utf-8'))
            print('DEBUG after sock.sendall with JSON')

            while True:
                data = sock.recv(1024)
                print(data.decode('utf-8'), end='')
                if len(data) < 1024:
                    # no more of this message, go back to waiting for next message
                    break
