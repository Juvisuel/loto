import random
from main import is_number
import classes

player1 = classes.Player("max", True)
player2 = classes.Player("evgen", True)
game1 = classes.Game()
game2 = classes.Game()


card1 = classes.Card(player1)
card2 = classes.Card(player2)
#
card1.print_card()
card2.print_card()


print(card1 == card2)
print(player1 == player2)
print(game1 == game2)