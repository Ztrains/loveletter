from typing import Dict, List
from game import Game

from player import Player


class Lobby:

    def __init__(self) -> None:
        #self.connectedPlayers: List[Player] = []    # list of players waiting in lobby
        self.connectedPlayers: Dict[str, Player] = {}
        self.isOpen: bool = True                    # is lobby is still open to new connections
        self.idCounter: int = 0                     # counter for player IDs

    # starts game if lobby is full (4 players)
    def isFull(self) -> bool:
        if self.isOpen:
            if len(self.connectedPlayers) == 4:     # 4 is max number of players
                print('lobby is full, game starting')
                game = Game(self.connectedPlayers)  # add class var? or create in server?
                self.isOpen = False                 # tells server game is started and sends cards
                return True
        else:
            # TODO: add logic to send to client attempting to connect that lobby is closed
            print('lobby is no longer open')
            return False
