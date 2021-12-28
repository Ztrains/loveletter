from typing import List
from card import Card
from hand import Hand

class Player:

    def __init__(self, name: str, playerID: int) -> None:
        self.isAlive: bool = True       # set to False if the player is knocked out of the round
        self.isProtected: bool = False  # set to True for handmaid protection
        self.isTurn: bool = False       # set to True if it is the player's turn
        self.hand: Hand = Hand()        # player's hand of cards
        self.wins: int = 0              # how many round wins (crowns) the player is
        self.name = name                # allow player to enter their name
        self.playerID = playerID        # player's ID for lobby (0, 1, 2, or 3)
#
#    @property
#    def isAlive(self):
#        return self.isAlive
#
#    @isAlive.setter
#    def isAlive(self, value: bool):
#        self.isAlive = value
#
#
#    @property
#    def isProtected(self):
#        return self.isProtected
#
#    @isProtected.setter
#    def isProtected(self, value: bool):
#        self.isProtected = value
#
#
#    @property
#    def isTurn(self):
#        return self.isTurn
#
#    @isTurn.setter
#    def isTurn(self, value: bool):
#        self.isTurn = value
#
#    
#    @property
#    def hand(self) -> List[Card]:
#        return self.hand
#
#    # probably not even needed
#    @hand.setter
#    def hand(self, value):
#        self.hand = value
#
#
#    @property
#    def wins(self):
#        return self.wins
#
#    @wins.setter
#    def wins(self, value: int):
#        self.wins = value
