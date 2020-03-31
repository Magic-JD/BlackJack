class HouseBettingRules:
    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum


class House:

    def __init__(self):
        self.house_rules = HouseBettingRules(2, 500)
        self.wallet = 1000000
        self.table = 0

    def describe_house_rules(self):
        print("""Bets must be in the range of the minimum and maximum bet, and must be a whole number.
The minimum is ${}, and the maximum is ${}.""".format(self.house_rules.minimum, self.house_rules.maximum))

    def accept_bet(self, bet):
        if self.house_rules.minimum <= bet <= self.house_rules.maximum:
            self.table += bet
            print("You have bet: ${}".format(bet))
            return True
        else:
            print("Your bet must be between ${} and ${}.".format(self.house_rules.minimum, self.house_rules.maximum))
            return False

    def take_winnings(self):
        self.wallet += self.table
        self.table = 0

    def give_winnings(self, winning_percentage):
        payout = (self.table * winning_percentage)
        self.wallet -= payout
        payout += self.table
        self.table = 0
        return payout

