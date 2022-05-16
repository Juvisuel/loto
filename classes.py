import pandas as pd
import random


# создание карточки игрока
def create_card():
    card_table = pd.DataFrame(columns=[i for i in range(9)], index=[0, 1, 2])

    all_numbers = [x for x in range(1, 90)]

    for i in card_table.index:
        numbers_line = []
        for j in card_table.columns:
            n_full = False
            while not n_full:
                number = random.randint(0, 9) + (j * 10)
                if number in all_numbers:
                    numbers_line.append(number)
                    all_numbers.pop(all_numbers.index(number))
                    n_full = True

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
    list_players1 = []

    for number in range(1, player_numbers + 1):
        print('игрок ', number)
        name1 = input('введите имя игрока ')
        live1 = False if input('это человек? 1 = да, 2 = нет ') == '2' else True
        list_players1.append(Player(name1, live1))

    return list_players1


class InitPlayers:

    def __init__(self):
        self.players = list_players()


# класс карточки
class Card:

    def __init__(self, player: object):
        self.card_table = create_card()
        self.name = player.name
        self.stat = 'game'

    def print_card(self):
        print(self.card_table)

        # for row in self.card_table.index:
        #     list_row = ' '.join([str(x) for x in (self.card_table.loc[row])])
        #     print(list_row)

    def __str__(self):
        return str(self.card_table.shape)

    def __eq__(self, other):
        sum1, sum2 = 0,0
        for x in self.card_table.columns:
            stolb = self.card_table[x]
            stolb_list = list(stolb)
            stolb_list_zeros = [x if type(x) == int else 0 for x in stolb_list]
            sum1 += sum(stolb_list_zeros)
        for x in other.card_table.columns:
            stolb = other.card_table[x]
            stolb_list = list(stolb)
            stolb_list_zeros = [x if type(x) == int else 0 for x in stolb_list]
            sum2 += sum(stolb_list_zeros)

        return sum1 == sum2


# игрок
name = '1'
live = True


class Player:

    def __init__(self, name1: object, live1: object):
        self.name = name1
        self.local_score = 0
        self.global_score = 0
        self.active = True
        self.live = live1
        self.card = Card(self)

    def __str__(self):
        return str(self.name)

    def __eq__(self, other):

        result = 0

        result += (self.name == other.name)
        result += (self.local_score == other.local_score)
        result += (self.global_score == other.global_score)
        result += (self.active == other.active)
        result += (self.live == other.live)

        return True if result == 5 else False



class Game:

    def __init__(self) -> object:
        self.status = 'open'
        self.steps = 0
        self.players = list_players()

    def __str__(self):
        return str(self.status)

    def __eq__(self, other):

        result = 0
        result += (self.status == other.status)
        result += (self.steps == other.steps)
        result += (self.players == other.players)

        return True if result == 3 else False



# печатается карточка текущего игрока

def print_all(player):
    print(f'______________{player.name}______________')
    print(player.card.print_card())
    decor_elem = '_' * len(player.name)
    print(f'______________{decor_elem}______________')
