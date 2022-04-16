class Inventory(object):
    foodInv = dict()
    drinkInv = dict()
    decorInv = dict()
    
    def __init__(self, name, objType, stats):
        self.name = name
        self.objType = objType
        self.stats = stats
        self.add(1)
    
    def add(self, num):
        if self.objType == 'food':
            if self.objType not in Inventory.foodInv:
                Inventory.foodInv[self] = num
            else:
                Inventory.foodInv[self] += num
        
        if self.objType == 'drink':
            if self.objType not in Inventory.drinkInv:
                Inventory.drinkInv[self] = num
            else:
                Inventory.drinkInv[self] += num
        
        if self.objType == 'decor':
            if self.objType not in Inventory.foodInv:
                Inventory.decorInv[self] = num
            else:
                Inventory.decorInv[self] += num
                
    def use(self, num):
        if self.objType == 'food':
            if num > Inventory.foodInv[self]:
                return False
            else:
                Inventory.foodInv[self] -= num
                return True
        if self.objType == 'drink':
            if num > Inventory.drinkInv[self]:
                return False
            else:
                Inventory.drinkInv[self] -= num
                return True
        if self.objType == 'decor':
            if num > Inventory.decorInv[self]:
                return False
            else:
                Inventory.decorInv[self] -= num
                return True
                
    
class Shop(object):
    def __init__(self, name, shopType):
        self.name = name
        self.shopType = shopType
        self.foodInv = dict()
        self.drinkInv = dict()
        self.decorInv = dict()
        self.inventory = [self.foodInv,self.drinkInv,self.decorInv]
        self.stockShop()
    
    def stockShop(self):
        if self.shopType == 'coffee':
            Cappuccino = shopInventory('cappuccino', 'drink', [-5, 20, 10], 5)
            self.drinkInv.append(Cappuccino)
            Latte = shopInventory('latte', 'drink', [-5, 15, 10], 5)
            self.drinkInv.append(Latte)
            Americano = shopInventory('americano', 'drink', [-5, 25, 10], 5)
            self.drinkInv.append(Americano)
        elif self.shopType == 'decor':
            Rug = shopInventory('rug', 'decor', [0, 0, 10], 15)
            self.decorInv.append(Rug)
            Lamp = shopInventory('lamp', 'decor', [0, 0, 15], 20)
            self.decorInv.append(Lamp)
            Plant = shopInventory('plant', 'decor', [0, 0, 20], 15)
            self.decorInv.append(Plant)
        elif self.shopType == 'grocery':
            Apple = shopInventory('apple', 'food', [10, 10, 10], 5)
            self.foodInv.append(Apple)
            Sandwich = shopInventory('sandwich', 'food', [20, 20, 20], 10)
            self.foodInv.append(Sandwich)
            GingerAle = shopInventory('gingerAle', 'drink', [-10, 15, 10], 5)
            self.drinkInv.append(GingerAle)
        elif self.shopType == 'asianGrocery':
            Seaweed = shopInventory('seaweed', 'food', [5, 5, 10], 5)
            self.foodInv.append(Seaweed)
            Ramen = shopInventory('ramen', 'food', [-15, 25, 20], 10)
            self.foodInv.append(Ramen)
            Yakult = shopInventory('yakult', 'drink', [5, 10, 10], 5)
            self.drinkInv.append(Yakult)
        
        self.shopRestock()
    
    def shopRestock(self):
        for item in self.inventory:
            item.restock(5)           

class shopInventory(Inventory):
    def __init__(self, name, objType, stats, price):
        super().__init__(name, objType, stats)
        self.price = price
    
    def sell(self, num):
        if self.objType == 'food':
            stockNum = shopInventory.foodInv[self.objType]
            if num > stockNum:
                return False
            else:
                shopInventory.foodInv[self.objType] -= num
        if self.objType == 'drink':
            stockNum = shopInventory.drinkInv[self.objType]
            if num > stockNum:
                return False
            else:
                shopInventory.drinkInv[self.objType] -= num
        if self.objType == 'decor':
            stockNum = shopInventory.decorInv[self.objType]
            if num > stockNum:
                return False
            else:
                shopInventory.decorInv[self.objType] -= num
        return self.price
    
    def restock(self, num):
        if self.objType == 'food':
            if self.objType not in shopInventory.foodInv:
                shopInventory.foodInv[self] = num
            else:
                shopInventory.foodInv[self] += num
        
        if self.objType == 'drink':
            if self.objType not in shopInventory.drinkInv:
                shopInventory.drinkInv[self] = num
            else:
                shopInventory.drinkInv[self] += num
        
        if self.objType == 'decor':
            if self.objType not in shopInventory.foodInv:
                shopInventory.decorInv[self] = num
            else:
                shopInventory.decorInv[self] += num

LaPrima = Shop('LaPrima', 'coffee')
print('--------------------')
print(LaPrima.name)
print('----------')
for item in LaPrima.inventory:
    print(f'{item.name}')
    print(f'{item.price} coins')
    print(f'health = {item.stats[0]}')
    print(f'energy = {item.stats[1]}')
    print(f'happiness = {item.stats[2]}')
    print('----------')

PandaMarket = Shop('PandaMarket', 'asianGrocery')
print('--------------------')
print(PandaMarket.name)
print('----------')
for item in PandaMarket.inventory:
    print(f'{item.name}')
    print(f'{item.price} coins')
    print(f'health = {item.stats[0]}')
    print(f'energy = {item.stats[1]}')
    print(f'happiness = {item.stats[2]}')
    print('----------')

DecorGalore = Shop('DecorGalore', 'decor')
print('--------------------')
print(DecorGalore.name)
print('----------')
for inventoryType in DecorGalore.inventory:
    for item in inventoryType:
        print(f'{item.name}')
        print(f'{item.price} coins')
        print(f'health = {item.stats[0]}')
        print(f'energy = {item.stats[1]}')
        print(f'happiness = {item.stats[2]}')
        print('----------')