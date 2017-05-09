from .shoe import Shoe
from .dealer import Dealer, DealerActions
from .player import PlayerActions
from .hand import HandStates

class Table:

    def __init__(self):
        self.shoe = Shoe()
        self.players = []
        self.dealer = Dealer()
        self.shoe.shuffle()


    #######################################################
    # Deal the initial first two cards to each player and the dealer
    def deal(self):
        for card_index in range(0,2):
            for player in self.players:
                player.add_card(player.hands[0], self.shoe.take_card())
            self.dealer.add_card(self.shoe.take_card())


    ##########################################################
    # Play hands until the shoe penetration has exceeded the max allowed
    def play_shoe(self):
        while(self.shoe.current_penetration < Shoe.max_penetration):

            # #place bets for each player
            for player in self.players:
                player.place_bet()

            #play hand for every player 
            self.play_round()

            #manage payouts (FIXME: pull into method?)
            for player in self.players:
                for hand in player.hands:
                    #blackjack
                    if(hand.state == HandStates._blackjack):
                        if(not self.dealer.hand.state == HandStates._blackjack):
                            player.bankroll += 1.5 * player.bet
                    #bust
                    elif(hand.state == HandStates._busted):
                        player.bankroll -= player.bet
                    #stand
                    elif(hand.state == HandStates._standing):
                        if(self.dealer.hand.state == HandStates._busted):
                            player.bankroll += player.bet
                        elif(self.dealer.hand.total > hand.total):
                            player.bankroll -= player.bet
                        elif(self.dealer.hand.total < hand.total):
                            player.bankroll += player.bet
                        #else push, so do nothing

            #reset player and dealer hands
            for player in self.players:
                player.reset()
            self.dealer.reset()
            
            for player_index in range(0, len(self.players)):
                print("Player " + str(player_index) + " Bankroll: " + str(self.players[player_index].bankroll))
            print("---------------------------------------")


    ######################################################
    # Play the hands for each player at the table
    def play_round(self):
        #deal initial cards
        self.deal()
        print(str(self.players[0].hands[0].cards[0].value) +  " + " + str(self.players[0].hands[0].cards[1].value) + ": ", end='')
        print(self.players[0].hands[0].total)
        print(self.dealer.up_card.value, end="")
        print(" (" + str(self.dealer.hand.cards[1].value) + ")")

        #check for player blackjacks
        for player_index in range(0, len(self.players)):
            self.check_for_player_blackjack(self.players[player_index])
        
        #play the hands for each player at the table if dealer does not have blackjack
        if(not self.dealer.hand.state == HandStates._blackjack):
            for player_index in range(0, len(self.players)):
                print("playing player hand")
                self.play_player_hands(self.players[player_index])

        #play the dealers Hand, only if there is at least one player in a non-busted state
        if(self.active_players()):
            print("playing dealer hand")
            self.play_dealer_hand()


        print("End player state: ", end="")
        print(self.players[0].hands[0].state)
        print("End dealer state: ", end="")
        print(self.dealer.hand.state)


    #################################################
    # Play all hands for a single player at the table
    def play_dealer_hand(self):
        hand_index = 0
        while self.dealer.hand.state == HandStates._active:
            action = self.dealer.take_action()
            print(action)
            self.handle_dealer_action(action)
            print("dealer total: " + str(self.dealer.hand.total))


    #################################################
    # Play all hands for a single player at the table
    def play_player_hands(self, player):
        hand_index = 0
        while(hand_index < len(player.hands)):
            print("new player hand")
            current_hand = player.hands[hand_index]
            while current_hand.state == HandStates._active:
                action = player.take_action(current_hand, self.dealer.up_card)
                print(action)
                self.handle_player_action(action, player, current_hand)
                print("player total: " + str(current_hand.total))
            hand_index +=1 
            

    ###########################################
    # Handle each dealer action based on type
    def handle_dealer_action(self, action):
        if(action == DealerActions._stand):
            self.dealer.hand.state = HandStates._standing
        elif(action == DealerActions._hit):
            self.dealer.add_card(self.shoe.take_card())


    ###########################################
    # Handle each player action based on type
    def handle_player_action(self, action, player, hand):
        if(action == PlayerActions._stand):
            hand.state = HandStates._standing
        elif(action == PlayerActions._hit):
            player.add_card(hand, self.shoe.take_card())
        elif(action == PlayerActions._split):
            player.split(hand)
        elif(action == PlayerActions._double):
            player.double(hand, self.shoe.take_card())
            hand.state = HandStates._standing


    ##########################################
    # Check to see if a player has a blackjack this round
    # Update state of hand to indicate blackjack if it exists
    def check_for_player_blackjack(self, player):
        if(len(player.hands) == 1 and player.hands[0].total == 21):
            player.hands[0].state = HandStates._blackjack
            return True
        else:
            return False

        
    #########################################
    # Check if any players are still active
    def active_players(self):
        for player in self.players:
            for hand in player.hands:
                if hand.state == HandStates._standing:
                    return True
        return False