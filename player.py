

class Player:

    def __init__(self, name: str) -> None:
        self.isAlive = True
        self.hand = []
        self.wins = 0
        self.name = name

    @property
    def isAlive(self):
        return self.isAlive

    @isAlive.setter
    def isAlive(self, value: bool):
        self.isAlive = value

    
    @property
    def hand(self):
        return self.hand

    @hand.setter
    def hand(self, value):
        self.hand = value


    @property
    def wins(self):
        return self.wins

    @wins.setter
    def wins(self, value: int):
        self.wins = value
