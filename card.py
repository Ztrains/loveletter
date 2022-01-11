from __future__ import annotations # needed for forward reference type hinting
import random, pprint
from typing import List

# class which holds all card definitions
class Card:

    # TODO: add function or similar to check which cards need a target, which are just played for self, etc.

    cardCount = [5, 2, 2, 2, 2, 1, 1, 1]
    cardNames = ['Guard', 'Priest', 'Baron', 'Handmaid', 'Prince', 'King', 'Countess', 'Princess']

    def __init__(self, power: int, name: str) -> None:
        self.power = power  # power of card (1 for guard, 8 for princess, etc.)
        self.name = name    # name of card (Baron, Prince, etc.)
      
    def newDeck() -> List[Card]:
        deck = []
        for power, count in enumerate(Card.cardCount, start=1):
            while(count > 0):
                card = Card(power, Card.cardNames[power-1])
                deck.append(card)
                count -= 1
        
        random.shuffle(deck)
        return deck

    def printDeck(deck):
        pprint.pprint([card.__dict__ for card in deck])

