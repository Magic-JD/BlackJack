from src.actions.action import Action
from src.actors.player import Player
from src.cards.deck import Deck


class Dealer(Player):

    def player_name(self):
        return "dealer"

    def __init__(self):
        super().__init__()
        self.deck = Deck()

    def deal(self, player, silent=False):
        card = self.deck.deal()
        if not silent:
            print("The dealer deals the {} to the {}".format(card, player.player_name()))
        player.hand.add_card(card)

    def __str__(self):
        return "Dealer:\n" + str(self.deck)

    def choose_action(self):
        print("Dealer has a hand with a value of {}.".format(self.hand.hand_value()))
        if self.hand.hand_value() < 17:
            print("Dealer must deal.")
            return Action.DEAL
        else:
            print("Dealer must stick.")
            return Action.STICK
