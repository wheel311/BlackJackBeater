
class Player:
    max_splits = 4
    max_splits_aces = 2

    def __init__(self, bankroll):
        reset(self)
        self.bankroll = bankroll
    

    #############################################
    # reset player values
    #############################################
    def reset(self):
        self.hands = []
        self.current_hand_index = 0
        self.bet = 0
        self.splits = 0
    

    #############################################
    # Determine bet based on strategy
    #############################################
    def bet(self):
        self.bet = 1


    #############################################
    # Take a card from the shoe
    #############################################
    def add_card(self, card):
        self.hands[self.current_hand_index].add


    #############################################
    # Take actions until finished with hand (bust or stand)
    #############################################
    def play_hand(self, dealer_card):
        pass


    #############################################
    # Determine action to take based on strategy
    #############################################
    def take_action(self, dealer_card):
        #-------------------------------------------------
        # handle splits
        if (len(self.hand == 2) and self.hand[0].value == self.hand[1] == value):
            #TODO: handle multiple hands per player for splits

        #-------------------------------------------------
        # handle when player has ace (and cannot split aces)
        elif (self.has_ace):
            pass

        #-------------------------------------------------
        # handle normal case
        else:
            pass

