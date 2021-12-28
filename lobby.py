from typing import List

from player import Player


class Lobby:

    def __init__(self) -> None:
        self.connectedPlayers: List[Player] = []    # list of players waiting in lobby
        self.isOpen: bool = True                    # is lobby is still open to new connections
        self.idCounter: int = 0                     # counter for player IDs

    # returns true if lobby is full (4 players)
    def isFull(self) -> bool:
        if self.connectedPlayers.count == 4:
            return True
        else: 
            return False
