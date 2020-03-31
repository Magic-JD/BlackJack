from src.actions.action import Action
from src.actors.player import Player


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
            if response.isdigit():
                bet_amount = int(response)
                if bet_amount < self.wallet:
                    bet = bet_amount
                else:
                    print("You don't have the funds to make that bet! You only have {}.".format(self.wallet))
            else:
                print("You must enter a whole number.")
        self.wallet -= bet
        return bet

    def update_wallet(self, money):
        self.wallet += money
        print("Your wallet value is: ${}".format(self.wallet))

    def choose_action(self):
        response = input("""Your hand has a value of {}.
Do you want another card [d] or to stick [s]?""".format(self.hand.hand_value()))
        while True:
            if response == "d":
                return Action.DEAL
            elif response == "s":
                return Action.STICK
            else:
                response = input("Please select either deal [d] or stick [s]")

    def get_user_action_input(self):
        return
