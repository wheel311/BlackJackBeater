from .card import Card
from enum import Enum

class HandStates(Enum):
	_active = 0
    _busted = 1
    _standing = 2
    

class Hand:

    def __init__(self):
        reset(self)


    def reset(self):
        self.cards = []
        self.total = 0
        self.has_ace = False
        self.has_blackjack = False
        self.state = HandStates._active

    
    def add_card(self, card):
        self.cards.append(card)
        self.total += card.value
        if (card.value == 1):
            self.has_ace = True