import random

from src.cards.card import Card
from src.cards.suit import Suit


class Deck:

    def __init__(self):
        self.cards = []

        for j in range(4):
            for i in range(1, 14):
                self.cards.append(Card(i, Suit(j)))
        self.shuffle()

    def __str__(self):
        pretty_string = ""
        for card in self.cards:
            pretty_string = pretty_string + str(card) + "\n"
        return pretty_string

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop(0)
