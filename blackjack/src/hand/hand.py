class Hand:

    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def hand_value(self):
        value = 0
        for card in self.cards:
            value += card.value
        if(value < 12) & any(map(lambda x: x.value == 1, self.cards)):
            value += 10
        return value

    def __str__(self):
        pretty_string = "Hand:\n"
        for card in self.cards:
            pretty_string = pretty_string + str(card) + "\n"
        return pretty_string
