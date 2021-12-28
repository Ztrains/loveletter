from __future__ import annotations # needed for forward reference type hinting
import random, pprint
from typing import List
from enum import Enum

# enum of card name to card power
class CardType(Enum):
    Guard = 1
    Priest = 2
    Baron = 3
    Handmaid = 4
    Prince = 5
    King = 6
    Countess = 7
    Princess = 8

# class which holds all card definitions
class Card():
    def __init__(self, power: int, name: str) -> None:
        self.power = power  # power of card (1 for guard, 8 for princess, etc.)
        self.name = name    # name of card (Baron, Prince, etc.)
