from src.actions.action import Action
from src.actors.player import Player


class Gambler(Player):

    def player_name(self):
        return "gambler"

    def choose_action(self):
        response = input("""Your hand has a value of {}.
Do you want another card [d] or to stick [s]?""".format(self.hand.hand_value()))
        if response == "d":
            return Action.DEAL
        else:
            return Action.STICK
