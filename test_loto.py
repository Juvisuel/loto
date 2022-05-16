import random
from main import is_number
import classes
import pandas as pd
import pytest
import pytest_cov


def test_card():
    card = classes.create_card()
    assert card.shape == (3, 9)
    assert min(set(card)) >= 0
    assert max(set(card)) < 90


def test_isnumber():
    card = classes.create_card()
    number = ' '
    while number == ' ':
        axis_1 = random.choice(range(3))
        axis_0 = random.choice(range(9))
        number = card[axis_0][axis_1]

    assert is_number(card, number)[0] == True
    assert is_number(card, number)[1] == [axis_0, axis_1]


class TestPlayers:
    name = 'max'
    live = True
    test_player = classes.Player(name, live)
    print(test_player)

    def test_player_name(self):
        assert self.name == 'max'

    def test_live(self):
        assert self.live == True

    def test_scores(self):
        self.test_player.local_score == 0
        self.test_player.global_score == 0

    def test_player_card(self):
        self.test_player.card.__class__ == object


class TestCard:
    test_card = classes.Card(player=classes.Player(name1='v', live1=True))

    def test_shape(self):
        self.test_card.card_table.shape == (3, 9)

    def test_card_content(self):
        assert min(set(self.test_card.card_table)) >= 0
        assert max(set(self.test_card.card_table)) < 90


class TestMagic:

    def __init__(self):
        self.player1 = classes.Player("max", True)
        self.player2 = classes.Player("evgen", True)
        self.game1 = classes.Game()
        self.game2 = classes.Game()
        self.card1 = classes.Card(self.player1)
        self.card2 = classes.Card(self.player2)

    def test_cards_eq(self):
        assert not (self.card1 == self.card2)

    def test_player(self):
        assert not (self.player1 == self.player2)

    def test_game(self):
        assert not (self.game1 == self.game2)
