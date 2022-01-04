import socketserver, pickle

from lobby import Lobby
from player import Player

# this class is in here instead of its own file just cause it's only this big
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True


class GameServer(socketserver.StreamRequestHandler):

    def handle(self):
        serverLobby: Lobby = self.server.lobby  # lobby obj created in the server obj below
        
        clientName = self.rfile.readline().decode('utf-8').strip()
        #print('DEBUG received name', clientName)
        self.wfile.write(f'Welcome, {clientName}'.encode('utf-8'))

        currentLobbyID = serverLobby.idCounter
        serverLobby.idCounter += 1

        serverLobby.connectedPlayers[clientName] = Player(clientName, currentLobbyID)

        print(clientName, 'connected from', self.client_address)

        # TODO: game only starts for last player to connect, need to fix
        # using events? or just put "while not serverLobby.isFull()"
        serverLobby.isFull()

        while True:
            if not serverLobby.isOpen:
                # probably should create Game obj here instead of in lobby?
                self.wfile.write('Lobby full, game starting'.encode('utf-8'))

                # TODO: need to send card drawn to client still
                playerCard = serverLobby.connectedPlayers[clientName].getCard()
                print(clientName, 'card drawn:', playerCard.name)
                self.wfile.write(pickle.dumps(playerCard))  # pickle serializes the card obj
                break


        while True:
            print('DEBUG in main event loop')
            data = self.rfile.readline()
            # Only when the client closed its end will readline return the empty string
            if not data:
                break
            self.wfile.write(data.decode('utf-8').upper().encode('utf-8'))

        serverLobby.connectedPlayers.pop(clientName)
        print(clientName, 'disconnected')

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
    server.lobby = Lobby()
    server.serve_forever()
