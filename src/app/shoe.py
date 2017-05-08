import random, math
from .card import *

class Shoe:

    max_penetration = .65

    def __init__(self, number_of_decks=6):
        self.card_index = 0
        self.cards = []
        self.current_penetration = 0

        # construct each card in the shoe
        for deck_index in range(number_of_decks):
            for suit_index in range(4):
                for value_index in range(1,14):

                    #set suit and value
                    if(value_index == 1):
                        value = 11
                    elif value_index >= 10:
                        value = 10
                    else:
                        value = value_index

                    if(suit_index == 0):
                        suit = "H"
                    elif (suit_index == 1):
                        suit = "D"
                    elif (suit_index == 2):
                        suit = "C"
                    elif (suit_index == 3):
                        suit = "S"
                    card = Card(value, suit)
                    self.cards.append(card)


    def shuffle(self):
        for iteration in range (10):
            for card_index in range(len(self.cards)):
                new_pos = math.floor( random.random() * 312)
                temp_card = self.cards[card_index]
                self.cards[card_index] = self.cards[new_pos]
                self.cards[new_pos] = temp_card


    def take_card(self):
        card = self.cards[self.card_index]
        self.card_index += 1
        self.current_penetration = self.card_index/len(self.cards)
        return card