import random, threading, time

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
        self.roundNum: int = 0          # what round number it currently is


    def startGame(self) -> None:
        random.shuffle(self.players)    # randomizes order of players
        self.startRound()
        self.isStarted = True
        self.gameLoop()
    
    def gameLoop(self):
        while True: 
            #playersInRound = list(self.players) # copy of self.players
            print('# of players still alive:', self.numPlayersStillAlive())   # counts # of player.isAlive == True
            while self.numPlayersStillAlive() > 1:       # while number of players with isAlive=True > 1 (more than one player alive)
                for player in self.players:
                    if self.numPlayersStillAlive == 1:
                        print('only 1 player left alive, round over')
                        break
                    if player.isAlive:
                        print(player.name, 'turn to play in Game.gameLoop()')
                        player.isTurn = True
                        
                        while player.isTurn is True:
                            # wait until isTurn is set to False after performing logic for player's turn
                            pass

                        # TODO: add some logic to wait for response from client, perform logic, then set isTurn to false and continue to next player

                    else:
                        print(player.name, 'is out, going to next player')
            
            # round over, start a new round
            roundWinner = next(player for player in self.players if player.isAlive is True)
            print('Round winner:', roundWinner.name)
            roundWinner.wins += 1
            self.startRound()

        
        

    def startRound(self):
        self.roundNum += 1
        print('Round', self.roundNum, 'starting')
        
        self.deck = Card.newDeck()
        Card.printDeck(self.deck)

        self.isInRound = True

        for player in self.players:
            player.addCardToHand(self.drawCard())
            player.isAlive = True


    def endGame(self):
        pass

    def isFull(self) -> None:
        print('DEBUG isFull len(self.players):', len(self.players))
        if self.isStarted:
            # TODO: add logic rejecting new connections if game already started
            pass
        if len(self.players) == self.maxPlayers:
            threading.Thread(target=self.startGame).start()
            #self.startGame()

    def numPlayersStillAlive(self) -> int:
        return len([player for player in self.players if player.isAlive is True])

    # TODO: this doesn't work properly if two players have the same name
    def getPlayerByName(self, name: str) -> Player:
        return next(player for player in self.players if player.name == name)
        
    def drawCard(self) -> Card:
        print('Drawing card, deck len now', len(self.deck) - 1)
        return self.deck.pop()

    # TODO: need to refactor all of the below playX functions
    def playCard(self, card: Card, player: Player, target: Player):
        if (card.power == 1):
            self.playGuard(player, target)
        elif (card.power == 2):
            self.playPriest(player, target)
        elif (card.power == 3):
            self.playBaron(player, target)
        elif (card.power == 4):
            self.playHandmaid(player)
        elif (card.power == 5):
            self.playPrince(player, target)
        elif (card.power == 6):
            self.playKing(player, target)
        elif (card.power == 7):
            # check for if countess can be played should be done client side
            self.playCountess(player)
        elif (card.power == 8):
            self.playPrincess(player)
        else: pass


    # additional logic still needs to be added for functions below

    def playGuard(self, player: Player, target: Player):

        # TODO: add logic to prompt player to guess card of target
        guess = '???'
        
        if (target.getCard().name == guess):
            target.isAlive = False
            # probably need more here
        else:
            pass


    def playPriest(self, player: Player, target: Player) -> Card: 

        # need to cast to Card type maybe?
        return target.getCard()
        

    def playBaron(self, player: Player, target: Player):

        # need logic for removing baron before comparison
        return player.getCard() > target.getCard()


    def playHandmaid(self, player: Player):
        # add snarky comment if you play handmaid 1st in the round

        # need to add logic in gameserver to set isProtected to False on player turn start
        player.isProtected = True


    def playPrince(self, player: Player, target: Player):

        discardedCard = target.hand.pop()
        # add logic to share discarded card with gameserver for all to see
        target.hand.append(Game.drawCard())


    def playKing(self, player: Player, target: Player):
        
        # add logic to remove king from hand before trade
        tradedCard = target.hand.pop()
        target.hand.append(player.hand.pop())
        player.hand.append(tradedCard)


    def playCountess(self, player: Player):

        # TODO: add logic where countess must be played if king/prince in hand
        ### should probably be done client side
        pass

    def playPrincess(self, player: Player):
        # Not sure why you'd want to play the princess...
        player.isAlive = False
