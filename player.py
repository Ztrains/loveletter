from typing import List
from card import Card

class Player:

    def __init__(self, name: str) -> None:
        self.isAlive: bool = True       # set to False if the player is knocked out of the round
        self.isProtected: bool = False  # set to True for handmaid protection
        self.isTurn: bool = False       # set to True if it is the player's turn
        self.hand: List[Card] = []      # player's hand of cards
        self.wins: int = 0              # how many round wins (crowns) the player is
        self.name = name                # allow player to enter their name

    def getCard(self) -> Card:          # returns card in players hand (assuming they only have 1)
        return self.hand[0]

    def addCardToHand(self, card: Card) -> None:
        self.hand.append(card)
