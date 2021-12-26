import random, pprint
from typing import List
from __future__ import annotations # needed for forward reference type hinting

# class which holds all card definitions
class Card:

    def __init__(self, power: int, name: str) -> None:
        self.power = power
        self.name = name
    
    guard = 1
    priest = 2
    baron = 3
    handmaid = 4
    prince = 5
    king = 6
    countess = 7
    princess = 8

    cards = [guard, priest, baron, handmaid, prince, king, countess, princess]
    cardCount = [5, 2, 2, 2, 2, 1, 1, 1]
    cardNames = ['Guard', 'Priest', 'Baron', 'Handmaid', 'Prince', 'King', 'Countess', 'Princess']

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

