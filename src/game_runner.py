
from src.actions.action import Action
from src.actors.dealer import Dealer
from src.actors.gambler import Gambler
from src.house_rules.house_betting_rules import house_rules


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
        print("""Bets must be in the range of the minimum and maximum bet, and must be a whole number.
The minimum is ${}, and the maximum is ${}.""".format(house_rules.minimum, house_rules.maximum))
        bet = Gambler.place_bet(self)
        print("You have bet: ${}".format(bet))
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
