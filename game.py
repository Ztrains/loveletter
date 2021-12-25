from card import Card
from player import Player


class Game:

    # for testing, remove later
    deck = Card.newDeck()
    Card.printDeck(deck)


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


    # all logic still needs to be added for functions below

    def playGuard(player: Player, target: Player):
        print('Guard played by ', player, 'against ', target)

    def playPriest(player: Player, target: Player):
        print('Priest played by ', player, 'against ', target)

    def playBaron(player: Player, target: Player):
        print('Baron played by ', player, 'against ', target)

    def playHandmaid(player: Player, target: Player):
        print('Handmaid played by ', player, 'against ', target)
        # add snarky comment if you play handmaid 1st in the round

    def playPrince(player: Player, target: Player):
        print('Prince played by ', player, 'against ', target)
        # add logic where countess must be played if king/prince in hand

    def playKing(player: Player, target: Player):
        print('King played by ', player, 'against ', target)
        # add logic where countess must be played if king/prince in hand

    def playCountess(player: Player, target: Player):
        print('Countess played by ', player, 'against ', target)
        # add logic where countess must be played if king/prince in hand

    def playPrincess(player: Player, target: Player):
        # Not sure why you'd want to play the princess...
        print('Princess played by ', player, 'against ', target)
