from src.actions.action import Action
from src.actors.player import Player
import math


def isDigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


class Gambler(Player):

    def __init__(self):
        super().__init__()
        self.wallet = 1000

    def player_name(self):
        return "gambler"

    def place_bet(self):
        bet = 0
        while bet == 0:
            response = input("Please place a bet... ")
            if isDigit(response):
                if float(response) % 1 == 0:
                    bet = int(response)
                    print("You have bet $" + str(bet))
                else:
                    bet = math.floor(float(response))
                    print("That's not a whole number. We will round it down to $" + str(bet))
            else:
                print("You must enter a number.")
        self.wallet -= bet
        return bet

    def update_wallet(self, money):
        self.wallet += money
        print("Your wallet value is: ${}".format(self.wallet))

    def choose_action(self):
        response = input("""Your hand has a value of {}.
Do you want another card [d] or to stick [s]?""".format(self.hand.hand_value()))
        if response == "d":
            return Action.DEAL
        else:
            return Action.STICK
