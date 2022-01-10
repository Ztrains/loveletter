import socketserver, pickle, time
from game import Game

from player import Player

# this class is in here instead of its own file just cause it's only this big
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True


class GameServer(socketserver.StreamRequestHandler):

    def handle(self):
        game: Game = self.server.game
        
        clientName = self.rfile.readline().decode('utf-8').strip()
        self.wfile.write(f'Welcome, {clientName}'.encode('utf-8'))

        game.players.append(Player(clientName))
        print(clientName, 'connected from', self.client_address)

        game.isFull()

        while True: # loop until game starts or client disconnects
            if game.isStarted:
                self.gameLoop(game, clientName)
                break # should break after client closes socket
            else:
                try: # probably a better way to do this to check if client is still connected
                    self.wfile.write('alive'.encode('utf-8'))
                except BrokenPipeError:
                    print('DEBUG client probably disconnect during try/except')
                    break
                time.sleep(1)

        # gets to here if client disconnects and socket gets closed
        currentPlayer = game.getPlayerByName(clientName)
        game.players.remove(currentPlayer)
        print(clientName, 'disconnected')

    def gameLoop(self, game: Game, clientName: str):
        print('in gameserver startGame()')
        self.wfile.write('Game started'.encode('utf-8'))
        currentPlayer = next(player for player in game.players if player.name == clientName)
        playerCard = currentPlayer.getCard()
        print(clientName, 'card drawn:', playerCard.name)
        self.wfile.write(pickle.dumps(playerCard))  # pickle serializes the card obj

        while True:
            print('DEBUG in main event loop')
            data = self.rfile.readline()
            # Only when the client closed its end will readline return the empty string
            if not data:
                break
            self.wfile.write(data.decode('utf-8').upper().encode('utf-8'))

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
