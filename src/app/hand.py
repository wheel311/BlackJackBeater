from .card import Card
from enum import Enum

class HandStates(Enum):
    _active = 0
    _busted = 1
    _standing = 2
    _blackjack = 3


class Hand:

    def __init__(self):
        self.reset()


    def reset(self):
        self.cards = []
        self.total = 0
        self.number_of_aces = 0
        self.has_blackjack = False
        self.state = HandStates._active

    
    def add_card(self, card):
        self.cards.append(card)
        self.total += card.value
        if (card.value == 11):
            self.number_of_aces +=1
        if(self.total > 21):
            if(self.number_of_aces > 0):
                self.number_of_aces -=1
                self.total -=10
            else:
                self.state = HandStates._busted


    def remove_last_card(self):
        card_to_remove = self.cards.pop()
        self.total -= card_to_remove.total
        if(card_to_remove.value == 11):
            self.number_of_aces -=1
        return card_to_remove