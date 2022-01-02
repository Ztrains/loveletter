import socketserver
from typing import List
from lobby import Lobby

from player import Player

# put this class in here instead of its own file just cause it's only this big
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

        isFull = serverLobby.isFull()
        if isFull:
            self.wfile.write('Lobby full, game starting'.encode('utf-8'))
        else:
            pass

        while True:
            data = self.rfile.readline()
            # Only when the client closed its end will readline return the empty string
            if not data:
                break
            self.wfile.write(data.decode('utf-8').upper().encode('utf-8'))

        serverLobby.connectedPlayers.pop(clientName)
        print(clientName, 'disconnected')


# server blocks on multiple clients, needs threading for each client
HOST, PORT = 'localhost', 8073
with ThreadedTCPServer((HOST, PORT), GameServer) as server:
    print('threaded socket server running')
    server.lobby = Lobby()
    server.serve_forever()
