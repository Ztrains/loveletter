import random

from typing import Dict, List
from card import Card
from player import Player


class Game:

    def __init__(self) -> None:
        self.deck: List[Card] = []      # the card deck for the game
        self.turn: Player = None        # whose turn it currently is
        self.players: List[Player] = [] # list of players connected to the game
        self.maxPlayers = 2             # max number of players before game starts
        self.isStarted: bool = False    # state of if game is started yet
        self.isInRound: bool = False    # state of if round is currently active


    def startGame(self) -> None:
        self.isStarted = True
        self.deck = Card.newDeck()
        self.isInRound = True
        random.shuffle(self.players)    # randomizes order of players
        Card.printDeck(self.deck)
        self.gameLoop()
    
    def gameLoop(self):
        while True: 
            while self.isInRound:       # loop for a round of the game
                pass
            
            # round over, get a new deck
            self.deck = Card.newDeck()

        
        

    def startRound(self):
        print('Round started')
        for player in self.players:
            player.addCardToHand(self.drawCard())


    def endGame(self):
        pass

    def isFull(self) -> None:
        if self.isStarted:
            # TODO: add logic rejecting new connections if game already started
            pass
        if len(self.players) == self.maxPlayers:
            self.startGame()

    # this doesn't work properly if two players have the same name
    def getPlayerByName(self, name: str) -> Player:
        return next(player for player in self.players if player.name == name)
        
    def drawCard(self) -> Card:
        print('Drawing card, deck size will be', len(self.deck) - 1)
        return self.deck.pop()

    # is it even worth having this function? (probably not)
    # could just check the card from gameserver when played and call appropriate func from there
    def playCard(card: Card, player: Player, target: Player):
        if (card.power == 1):
            Game.playGuard(player, target)
        elif (card.power == 2):
            Game.playPriest(player, target)
        elif (card.power == 3):
            Game.playBaron(player, target)
        elif (card.power == 4):
            Game.playHandmaid(player, target)
        elif (card.power == 5):
            Game.playPrince(player, target)
        elif (card.power == 6):
            Game.playKing(player, target)
        elif (card.power == 7):
            if (any(card.name == 'King' or card.name == 'Prince' for card in player.hand)):
                print('can\'t play countess, you have a king or prince in your hand')
            else:
                Game.playCountess(player, target)
        elif (card.power == 8):
            Game.playPrincess(player, target)
        else: pass


    # additional logic still needs to be added for functions below

    def playGuard(player: Player, target: Player):
        print('Guard played by ', player, 'against ', target)

        # TODO: add logic to prompt player to guess card of target
        guess = '???'
        
        if (target.getCard().name == guess):
            target.isAlive = False
            # probably need more here
        else:
            pass


    def playPriest(player: Player, target: Player) -> Card: 
        print('Priest played by ', player, 'against ', target)

        # need to cast to Card type maybe?
        return target.getCard()
        

    def playBaron(player: Player, target: Player):
        print('Baron played by ', player, 'against ', target)

        # need logic for removing baron before comparison
        return player.getCard() > target.getCard()


    def playHandmaid(player: Player, target: Player):
        print('Handmaid played by ', player, 'against ', target)
        # add snarky comment if you play handmaid 1st in the round

        # need to add logic in gameserver to set isProtected to False on player turn start
        player.isProtected = True


    def playPrince(player: Player, target: Player):
        print('Prince played by ', player, 'against ', target)

        discardedCard = target.hand.pop()
        # add logic to share discarded card with gameserver for all to see
        target.hand.append(Game.drawCard())


    def playKing(player: Player, target: Player):
        print('King played by ', player, 'against ', target)
        
        # add logic to remove king from hand before trade
        tradedCard = target.hand.pop()
        target.hand.append(player.hand.pop())
        player.hand.append(tradedCard)


    def playCountess(player: Player, target: Player):
        print('Countess played by ', player, 'against ', target)

        # add logic where countess must be played if king/prince in hand
        pass

    def playPrincess(player: Player, target: Player):
        # Not sure why you'd want to play the princess...
        print('Princess played by ', player, 'against ', target)
        player.isAlive = False
