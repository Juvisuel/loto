import classes
from main import game_play


classes.decor_card()
print('добро пожаловать в игру. Выберите, что будем делать')
print('1 - играем')
print('2 - не играем')
classes.decor_card()
game = []

choice = int(input('введите число: '))

if choice == 1:

    game = classes.Game()
    barrels = [x for x in range(1, 91)]

    print()
    print('карты розданы')

    game_end = game_play(game, barrels)

    if game.status == 'fin':
        print('спасибо за игру')

else:
    print('до встречи')
