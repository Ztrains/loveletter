from typing import List
from card import Card, CardType
from player import Player
from deck import Deck

class Game:

    def __init__(self, players: List[Player]) -> None:
        self.deck: Deck = Deck()                # the card deck for the game
        self.turn: Player = None                # whose turn it currently is
        self.players: List[Player] = players    # list of players in the game

        Deck.printDeck()                        # prints deck for testing

    # is it even worth having this function? (probably not)
    # could just check the card from gameserver when played and call appropriate func from there
    def playCard(card: Card, player: Player, target: Player):
        if (card.power == CardType.Guard):
            Game.playGuard(player, target)
        elif (card.power == CardType.Priest):
            Game.playPriest(player, target)
        elif (card.power == CardType.Baron):
            Game.playBaron(player, target)
        elif (card.power == CardType.Handmaid):
            Game.playHandmaid(player, target)
        elif (card.power == CardType.Prince):
            Game.playPrince(player, target)
        elif (card.power == CardType.King):
            Game.playKing(player, target)
        elif (card.power == CardType.Countess):
            if (any(card.power == CardType.Prince or card.power == CardType.King for card in player.hand)):
                print('can\'t play countess, you have a king or prince in your hand')
            else:
                Game.playCountess(player, target)
        elif (card.power == CardType.Princess):
            Game.playPrincess(player, target)

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
        target.hand.append(Game.deck.drawCard())


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
