from __future__ import annotations # needed for forward reference type hinting
import random, pprint
from typing import List
from card import Card, CardType

class Deck:
	def __init__(self) -> None:
		self.deck: List[Card] = []
		cardCount = [5, 2, 2, 2, 2, 1, 1, 1]
		for power, count in enumerate(cardCount, start=1):
			self.deck.append(Card(power, CardType(power)) for _ in range(count))

		self.shuffle()

	def shuffle(self) -> None:
		random.shuffle(self.deck)

	def draw(self) -> Card:
		return self.deck.pop()

	def printDeck(self) -> None:
		pprint.pprint([card.__dict__ for card in self.deck])