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
        
        currentLobbyID = serverLobby.idCounter
        serverLobby.idCounter += 1

        serverLobby.connectedPlayers.append(Player(f'Player{currentLobbyID}', \
            currentLobbyID))
        print(serverLobby.connectedPlayers[currentLobbyID].name, 'connected from', \
            self.client_address)

        while True:
            data = self.rfile.readline()
            # Only when the client closed its end will readline return the empty string
            if not data:
                break
            self.wfile.write(data.decode('utf-8').upper().encode('utf-8'))

        # TODO: add logic to remove player from lobby.connectedPlayers here
        print(serverLobby.connectedPlayers[currentLobbyID].name, 'disconnected')


# server blocks on multiple clients, needs threading for each client
HOST, PORT = 'localhost', 8073
with ThreadedTCPServer((HOST, PORT), GameServer) as server:
    print('threaded socket server running')
    server.lobby = Lobby()
    server.serve_forever()
