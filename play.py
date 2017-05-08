from src.app.table import Table
from src.app.player import Player

##################################################
# Initialize the Table
##################################################
table = Table()
table.shoe.shuffle()

table.players.append(Player(1000))

table.play_shoe()