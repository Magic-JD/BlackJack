from src.cards.suit import Suit


class Card:

    def __init__(self, card_number, suit):
        if card_number == 1:
            self.name = "A"
            self.value = card_number
        elif card_number == 11:
            self.name = "J"
            self.value = 10
        elif card_number == 12:
            self.name = "Q"
            self.value = 10
        elif card_number == 13:
            self.name = "K"
            self.value = 10
        else:
            self.name = str(card_number)
            self.value = card_number
        self.suit = suit

    def __str__(self):
        return self.name + " of " + self.suit.name
