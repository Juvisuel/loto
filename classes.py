import pandas as pd
import random


# создание карточки игрока
def create_card():
    card_table = pd.DataFrame(columns=[i for i in range(9)], index=[0, 1, 2])

    for i in card_table.index:
        numbers_line = []
        for j in card_table.columns:
            number = random.randint(0, 9) + (j * 10)
            numbers_line.append(number)

        zeros = random.sample(range(9), 3)

        for j in zeros:
            numbers_line[j] = ' '
        card_table.loc[i] = numbers_line

    return card_table

# просто длинная полоса
def decor_card():
    print('_' * 100)



# создание списка игроков

def list_players():
    player_numbers = int(input('введите количество игроков: '))
    list_players = []

    for number in range(1, player_numbers + 1):
        print('игрок ', number)
        list_players.append(Player())

    return list_players


class Initplayers:

    def __init__(self):
        self.players = list_players()






# класс карточки
class Card:

    def __init__(self, player):
        self.card_table = create_card()
        self.name = player.name
        self.stat = 'game'

    def print_card(self):
        print(self.card_table)

        # for row in self.card_table.index:
        #     list_row = ' '.join([str(x) for x in (self.card_table.loc[row])])
        #     print(list_row)


# игрок

class Player:

    def __init__(self):
        self.name = input('введите имя игрока ')
        self.local_score = 0
        self.global_score = 0
        self.active = False
        self.live = False if input('это человек? 1 = да, 2 = нет ') == '2' else True
        self.card = Card(self)


class Game:

    def __init__(self):
        self.status = 'open'
        self.steps = 0
        self.players = list_players()


# печатается карточка текущего игрока

def print_all(player):
    print(f'______________{player.name}______________')
    print(player.card.print_card())
    decor_elem = '_'*len(player.name)
    print(f'______________{decor_elem}______________')