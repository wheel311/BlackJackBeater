from enum import Enum
from .hand import Hand, HandStates

class DealerActions(Enum):
    _hit = 0
    _stand = 1

class Dealer:

    def __init__(self):
        self.hand = Hand()
        self.up_card = None

    #############################################
    # Add a card to dealer's hand
    #############################################
    def add_card(self, card):
        self.hand.add_card(card)
        if(len(self.hand.cards) == 1):
            self.up_card = card
        if(len(self.hand.cards) == 2 and self.hand.total == 21):
            self.hand.state == HandStates._blackjack

    ######################################################
    # Take action until a stand or bust
    def take_action(self):
        if(self.hand.total < 17):
            return DealerActions._hit
        else:
            return DealerActions._stand