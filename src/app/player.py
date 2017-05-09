from .hand import Hand, HandStates
from enum import Enum

class PlayerActions(Enum):
    _hit = 0
    _stand = 1
    _split = 2
    _double = 3


class Player:
    _max_splits = 4
    _max_splits_aces = 2

    def __init__(self, bankroll):
        self.reset()
        self.bankroll = bankroll
    

    #############################################
    # reset player values
    #############################################
    def reset(self):
        self.hands = [Hand()]
        self.bet = 0
        self.splits = 0
    

    #############################################
    # Determine bet based on strategy
    #############################################
    def place_bet(self):
        self.bet = 1


    #############################################
    # Add a card to one of the player's hands
    #############################################
    def add_card(self, hand, card):
        if(len(hand.cards) >= 2):
            print("\t" + str(card.value))
        hand.add_card(card)

    #############################################
    # Add a card to one of the player's hands
    #############################################
    def double(self, hand, card):
        self.bet *=2
        hand.add_card(card)


    ############################################
    # Execute split
    ############################################
    def split(self, hand):
        removed_card = hand.remove_last_card()
        self.hands.append(Hand())
        new_hand = self.hands[-1]
        new_hand.add_card(removed_card)


    #############################################
    # Determine action to take based on strategy
    #############################################
    def take_action(self, hand, dealer_card):
        #-------------------------------------------------
        # handle cases where player should split
        if (len(hand.cards) == 2 and hand.cards[0].value == hand.cards[1].value):
            split_card_value = hand.cards[0].value

            if(split_card_value == 2 or split_card_value == 3):
                if(dealer_card.value >=2 and dealer_card.value <= 7):
                    return PlayerActions._split
            if(split_card_value == 4):
                if(dealer_card.value >=5 and dealer_card.value <=6):
                    return PlayerActions._split
            if(split_card_value == 6):
                if(dealer_card.value >=2 and dealer_card.value <=6):
                    return PlayerActions._split
            if(split_card_value == 7):
                if(dealer_card.value >=2 and dealer_card.value <=7):
                    return PlayerActions._split
            if(split_card_value == 9):
                if((dealer_card.value >=2 and dealer_card.value <=6) or 
                    (dealer_card.value >=8 and dealer_card.value <=9)):
                    return PlayerActions._split
            if(split_card_value == 8 or split_card_value == 11):
                return PlayerActions._split

        #-------------------------------------------------
        # handle when player has ace (and cannot split aces)
        if (hand.number_of_aces > 0):
            if(hand.total == 13 or hand.total == 14):
                if(len(hand.cards) == 2 and dealer_card.value >=5 and dealer_card.value <=6):
                    return PlayerActions._double
                else:
                    return PlayerActions._hit
            if(hand.total == 15 or hand.total == 16):
                if(len(hand.cards) == 2 and dealer_card.value >=4 and dealer_card.value <=6):
                    return PlayerActions._double
                else:
                    return PlayerActions._hit
            if(hand.total == 17):
                if(len(hand.cards) == 2 and dealer_card.value >=3 and dealer_card.value <=6):
                    return PlayerActions._double
                else:
                    return PlayerActions._hit
            if(hand.total == 18):
                if(len(hand.cards) == 2 and dealer_card.value >=3 and dealer_card.value <=6):
                    return PlayerActions._double
                elif(dealer_card.value == 2 or dealer_card.value >=7 and dealer_card.value <=8):
                    return PlayerActions._stand
                else:
                    return PlayerActions._hit
            

        #-------------------------------------------------
        # handle normal case, if above cases didn't return
        if(hand.total <= 8):
            return PlayerActions._hit
        if(hand.total == 9):
            if(len(hand.cards) == 2 and dealer_card.value >=3 and dealer_card.value <=6):
                return PlayerActions._double
            else:
                return PlayerActions._hit
        if(hand.total == 10):
            if(len(hand.cards) == 2 and dealer_card.value >=2 and dealer_card.value <=9):
                return PlayerActions._double
            else:
                return PlayerActions._hit
        if(hand.total == 11):
            if(len(hand.cards) == 2 and dealer_card.value >=2 and dealer_card.value <=10):
                return PlayerActions._double
            else:
                return PlayerActions._hit
        if(hand.total == 12 ):
            if(dealer_card.value >=4 and dealer_card.value <=6):
                return PlayerActions._stand
            else:
                return PlayerActions._hit
        if(hand.total >= 13 and hand.total <= 16 ):
            if(dealer_card.value >=2 and dealer_card.value <=6):
                return PlayerActions._stand
            else:
                return PlayerActions._hit
        if(hand.total >= 17 ):
            return PlayerActions._stand

        
        print("OOPS: " + str(hand.total) + " : " + str(dealer_card.value))
        raise Exception('Case not handled by player strategy')
    # END take_action
