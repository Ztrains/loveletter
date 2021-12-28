from __future__ import annotations # needed for forward reference type hinting
import random, pprint
from typing import List
from card import Card, CardType

class Hand:
	def __init__(self) -> None:
		self.hand: List[Card] = []

	def getCard(self) -> Card:
		return self.hand[0]

	def addCard(self, card: Card):
		self.hand.append(card)

	def removeCard(self, card: Card):
		self.hand.remove(card)

	def discardCard(self):
		return self.hand.pop()