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

    def player_name(self):
        return "gambler"

    def place_bet(self):
        bet = 0
        while bet == 0:
            response = input("Please place a bet... ")
            if isDigit(response):
                if 2 <= float(response) <= 500:
                    if float(response) % 1 == 0:
                        bet = int(response)
                        print("You have bet $" + str(bet))
                    else:
                        bet = math.floor(float(response))
                        print("That's not a whole number. We will round it down to $" + str(bet))
                else:
                    print("Your bet must be between $2 and $500.")
            else:
                print("You must enter a number.")
        return bet


    def choose_action(self):
        response = input("""Your hand has a value of {}.
Do you want another card [d] or to stick [s]?""".format(self.hand.hand_value()))
        if response == "d":
            return Action.DEAL
        else:
            return Action.STICK
