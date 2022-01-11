import socketserver, pickle, time, json
from typing import Dict
from card import Card
from game import Game

from player import Player

# this class is in here instead of its own file just cause it's only this big
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True


class GameServer(socketserver.StreamRequestHandler):

    # figure out how to overload constructor properly with this StreamRequestHandler inheritance

    def handle(self):
        game: Game = self.server.game
        
        self.clientName = self.rfile.readline().decode('utf-8').strip()
        self.wfile.write(f'Welcome, {self.clientName}'.encode('utf-8'))

        game.players.append(Player(self.clientName))
        print(self.clientName, 'connected from', self.client_address)

        game.isFull()
        #print(self.clientName, '@@@0')
        while True: # loop until game starts or client disconnects
            if game.isStarted:
                #print(self.clientName, '@@@1')
                self.gameLoop()
                break # should break after client closes socket
            else:
                #print(self.clientName, '@@@2')
                try: # probably a better way to do this to check if client is still connected
                    self.wfile.write('alive'.encode('utf-8'))
                except BrokenPipeError:
                    print('DEBUG client probably disconnect during try/except')
                    break
                time.sleep(1)

        # gets to here if client disconnects and socket gets closed
        #print(self.clientName, '@@@3')
        currentPlayer = game.getPlayerByName()
        game.players.remove(currentPlayer)
        print(self.clientName, 'disconnected')

    def gameLoop(self):
        game: Game = self.server.game
        #print(self.clientName, '@@@4')
        print('in gameserver startGame()')
        self.wfile.write('Game started'.encode('utf-8'))
        currentPlayer = next(player for player in game.players if player.name == self.clientName)
        playerCard = currentPlayer.getCard()
        print(self.clientName, 'card drawn:', playerCard.name)
        self.wfile.write(pickle.dumps(playerCard))  # pickle serializes the card obj

        while True:
            #print('DEBUG in main event loop')
            
            self.waitForTurn()

            # client's turn when it gets to here
            print('DEBUG server waiting for', self.clientName, 'to take turn and send data')
            data = self.rfile.readline()
            # Only when the client closed its end will readline return the empty string
            if not data:
                break
            self.wfile.write(data.decode('utf-8').upper().encode('utf-8'))

    # client needs to wait for their turn to play
    def waitForTurn(self):
        game: Game = self.server.game
        print(self.clientName, 'is waiting for their turn')
        while not game.getPlayerByName(self.clientName).isTurn:
            # wait here until it is the client's turn
            pass

        print(self.clientName, 'turn to play in Gameserver.waitForTurn()')
        self.wfile.write('Your turn'.encode('utf-8'))   # inform client is is their turn

        newCard: Card = game.drawCard()
        game.getPlayerByName(self.clientName).addCardToHand(newCard)
        print(self.clientName, 'card drawn:', newCard.name)
        self.wfile.write(pickle.dumps(newCard))  # pickle serializes the card obj

        print('DEBUG 2nd card sent to', self.clientName, ', waiting for their turn')
        data = self.rfile.readline().decode('utf-8')           # read data from client
        receivedMove: Dict[str, str] = json.loads(data)

        for key, val in receivedMove.items():
            print('key:', key, 'val:', val)

        print('receivedMove[name]:', receivedMove['cardName'])
        print('receivedMove[target]:', receivedMove['target'])
        

    # TODO: need to create msg structure for client/server communications (json?)
    def sendToClient():
        # may need to figure out how to call this from Game class to separate game/network logic
        pass

    # TODO: add parsing logic of msgs (use pickle library?)
    def receiveFromClient():
        # TODO: probably should parse msg here but perform actual logic in Game class
        pass


# server blocks on multiple clients, needs threading for each client
HOST, PORT = 'localhost', 8073
with ThreadedTCPServer((HOST, PORT), GameServer) as server:
    print('threaded socket server running')
    server.game = Game()
    server.serve_forever()
