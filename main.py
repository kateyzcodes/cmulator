from cmu_cs3_graphics import *
from campus import *
from grades import *
from relationship import *
from shops import *
from utilityf import *
from student import *
from inventory import *
from wallet import *

# demo main file
        
# initialize a student
Katelyn = Student('Katelyn', 'Zheng', CompSci)

# show Bars
barsList = Katelyn.getBars()
for bar in barsList:
    print(f'{bar.name} bar = {bar.level}')
print('----------')

# show how change in Bars can affect next best action
Katelyn.health.level-=50
for bar in barsList:
    print(f'{bar.name} bar = {bar.level}')
print(f'next best action is {getNextBestStep(Katelyn)}')

# # stock inventory, buy things, shopping
# Cappuccino = shopItem('cappuccino', 'drink', [-5, 20, 10], 5)
# Latte = shopItem('latte', 'drink', [-5, 15, 10], 5)
# Americano = shopItem('americano', 'drink', [-5, 25, 10], 5)
# Apple = shopItem('apple', 'food', [10, 10, 10], 5)
# Sandwich = shopItem('sandwich', 'food', [20, 20, 20], 10)
# GingerAle = shopItem('gingerAle', 'drink', [-10, 15, 10], 5)
# Rug = shopItem('rug', 'decor', [0, 0, 10], 15)
# Lamp = shopItem('lamp', 'decor', [0, 0, 15], 20)
# Plant = shopItem('plant', 'decor', [0, 0, 20], 15)

# Entropy.sell(Apple, 2)
# LaPrima.sell(Latte, 1)
# DecorGalore.sell(Plant, 3)
# Katelyn.inventory.buy(Entropy, Apple, 2)
# Katelyn.inventory.buy(LaPrima, Latte, 1)
# Katelyn.inventory.buy(DecorGalore, Plant, 3)

# # demonstrate inventory and wallet
# for invType in Inventory.inventory:
#     print(invType)
#     print('----------')
#     for item in invType:
#         print(f'{invType[item]} {item.name}')
#     print('__________')
