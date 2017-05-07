from .shoe import Shoe

class Table:

    def __init__(self):
        self.shoe = Shoe()
        self.players = []
        self.shoe.shuffle()


    def deal(self):
        for card_index in range(0,2):
            for player_index in range(0, self.players.length):
                self.players[player_index].add_card(self.shoe.take_card())


    def play_shoe(self):
        pass

    