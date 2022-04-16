from wallet import *
from shops import *
# Inventory

class Inventory(object):
    foodInv = dict()
    drinkInv = dict()
    decorInv = dict()
    inventory = [foodInv,drinkInv,decorInv]
    def __init__(self, person):
        self.person = person
    
    def buy(self, shop, item, num):
        sale = shop.sell(item, num)
        if sale != False:
            totalPrice = sale*num
            funds = self.wallet.purchase(totalPrice)
            if funds == True:
                # add to food
                if item.objType == 'food':
                    if item not in Inventory.foodInv:
                        Inventory.foodInv[item] = num
                    else:
                        Inventory.foodInv[item] += num
                # add to drinks
                if item.objType == 'drink':
                    if item not in Inventory.drinkInv:
                        Inventory.drinkInv[item] = num
                    else:
                        Inventory.drinkInv[item] += num
                # add to decor
                if item.objType == 'decor':
                    if item not in Inventory.decorInv:
                        Inventory.decorInv[item] = num
                    else:
                        Inventory.decorInv[item] += num
                return True
        return False
    
    @staticmethod
    def use(item):
        if item.objType == 'food':
            if item in Inventory.foodInv:
                if Inventory.foodInv[item] > 0:
                    Inventory.foodInv[item] -= 1
                    return True
        elif item.objType == 'drink':
            if item in Inventory.drinkInv:
                if Inventory.drinkInv[item] > 0:
                    Inventory.drinkInv[item] -= 1
                    return True
        elif item.objType == 'decor':
            if item in Inventory.decorInv:
                if Inventory.decorInv[item] > 0:
                    Inventory.decorInv[item] -= 1
                    return True
        return False
        
