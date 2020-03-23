
from src.actions.action import Action
from src.actors.dealer import Dealer
from src.actors.gambler import Gambler


class GameRunner:

    def __init__(self):
        self.dealer = Dealer()
        self.gambler = Gambler()
        for i in range(2):
            self.dealer.deal(self.gambler, True)
            self.dealer.deal(self.dealer, True)

    def player_choice(self, player):
        action = player.choose_action()
        while action == Action.DEAL:
            self.dealer.deal(player)
            if player.is_bust():
                break
            action = player.choose_action()

    def run_game(self):
        print("This is your hand")
        print(self.gambler.hand)
        self.player_choice(self.gambler)
        if self.gambler.is_bust():
            print("You are bust! You lose :(")
        else:
            print("Your final score is {}".format(self.gambler.hand.hand_value()))
            self.player_choice(self.dealer)
            if self.dealer.hand.hand_value() > self.gambler.hand.hand_value():
                print("The dealer beat you this time!!!")
            else:
                print("Congratulations, you won!!!")
