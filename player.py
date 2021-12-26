

from typing import List
from card import Card


class Player:

    def __init__(self, name: str) -> None:
        self.isAlive: bool = True
        self.isProtected: bool = False  # for handmaid protection
        self.isTurn: bool = False
        self.hand: List[Card] = []
        self.wins: int = 0
        self.name = name

    def getCard(self) -> Card:
        return self.hand[0]

    @property
    def isAlive(self):
        return self.isAlive

    @isAlive.setter
    def isAlive(self, value: bool):
        self.isAlive = value


    @property
    def isProtected(self):
        return self.isProtected

    @isProtected.setter
    def isProtected(self, value: bool):
        self.isProtected = value


    @property
    def isTurn(self):
        return self.isTurn

    @isTurn.setter
    def isTurn(self, value: bool):
        self.isTurn = value

    
    @property
    def hand(self) -> List[Card]:
        return self.hand

    # probably not even needed
    @hand.setter
    def hand(self, value):
        self.hand = value


    @property
    def wins(self):
        return self.wins

    @wins.setter
    def wins(self, value: int):
        self.wins = value
