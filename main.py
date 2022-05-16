import random
import classes


def is_number(table, number):

    indexes = []
    result = False
    for j in table.columns:
        for i in table.index:
            if table.loc[i, j] == number:
                result = True
                indexes = [j, i]
    print('в коде', table, number,indexes)

    return result, indexes


def cross_card(player_temp, game_temp, indexes):

    player_temp.card.card_table[indexes[0]][indexes[1]] = '-'
    print('зачеркнуто')

    if sum(player_temp.card.card_table) == 0:
        player_temp.card.stat = 'win'
        game_temp.status == 'fin'

    return player_temp.card, game_temp


def barrels_pop(barrels):

    barrel_number = random.choice(barrels)
    barrels.pop(barrels.index(barrel_number))

    return barrel_number, barrels


def round(game_temp, barrels):

    barrel_number, barrels1 = barrels_pop(barrels)
    if sum(barrels1) == 0:
        game_temp.status = 'fin'

    if game_temp.status == 'open':

        for player in game_temp.players:

            if player.card.stat == 'game' and player.live:
                print('шаг игры ', game_temp.steps, ' выпал номер: ** {} ** '.format(barrel_number))
                classes.print_all(player)
                choice = int(input('зачеркиваем? (1 = да, 2 = нет)'))

                if choice == 1:
                    print(1)
                    is_num, indexes = is_number(player.card.card_table, barrel_number)
                    print('проверка выбора',is_num, indexes  )
                    if is_num:
                        print('номер: ** {} ** есть на карте игрока {}!'.format(barrel_number, player.name))
                        player.card, game_temp = cross_card(player, game_temp, indexes)

                    else:
                        print('ошибка! номера ** {} ** нет на карте игрока, вы проиграли {}!'.format(barrel_number,
                                                                                                     player.name))
                        player.card.stat = 'lose'
                        game_temp.status == 'fin'

            elif player.card.stat == 'game' and not player.live:

                is_num, indexes = is_number(player.card.card_table, barrel_number)
                if is_num:
                    print('номер: ** {} ** есть на карте игрока {}!'.format(barrel_number, player.name))
                    player.card, game_temp = cross_card(player, game_temp, indexes)

    active_players = 0
    for player in game_temp.players:
        if player.card.stat == 'game':
            active_players += 1

    if active_players < 1:
        game_temp.status = 'fin'

    game_temp.steps += 1
    game = game_temp

    return game, barrels1


def game_play(game, barrels):
    game_temp = game

    while sum(barrels) > 0:

        game_temp, barrels1 = round(game_temp, barrels)
        barrels = barrels1
        if game_temp.status == 'fin':
            break
    print()

    return game_temp




