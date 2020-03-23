from abc import ABC, abstractmethod

from src.hand.hand import Hand


class Player(ABC):

    def __init__(self):
        self.hand = Hand()

    def is_bust(self):
        return self.hand.hand_value() > 21

    @abstractmethod
    def choose_action(self):
        pass

    @abstractmethod
    def player_name(self):
        pass

