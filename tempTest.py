import random

barrels = [x for x in range(1, 91)]
barrel_number = random.choice(barrels)
barrels.pop(barrels.index(barrel_number))
print(barrels, barrel_number)