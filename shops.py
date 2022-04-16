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
            Cappuccino = shopItem('cappuccino', 'drink', [-5, 20, 10], 5)
            self.drinkInv[Cappuccino] = 0
            Latte = shopItem('latte', 'drink', [-5, 15, 10], 5)
            self.drinkInv[Latte] = 0
            Americano = shopItem('americano', 'drink', [-5, 25, 10], 5)
            self.drinkInv[Americano] = 0
        elif self.shopType == 'decor':
            Rug = shopItem('rug', 'decor', [0, 0, 10], 15)
            self.decorInv[Rug] = 0
            Lamp = shopItem('lamp', 'decor', [0, 0, 15], 20)
            self.decorInv[Lamp] = 0
            Plant = shopItem('plant', 'decor', [0, 0, 20], 15)
            self.decorInv[Plant] = 0
        elif self.shopType == 'grocery':
            Apple = shopItem('apple', 'food', [10, 10, 10], 5)
            self.foodInv[Apple] = 0
            Sandwich = shopItem('sandwich', 'food', [20, 20, 20], 10)
            self.foodInv[Sandwich] = 0
            GingerAle = shopItem('gingerAle', 'drink', [-10, 15, 10], 5)
            self.drinkInv[GingerAle] = 0
        elif self.shopType == 'asianGrocery':
            Seaweed = shopItem('seaweed', 'food', [5, 5, 10], 5)
            self.foodInv[Seaweed] = 0
            Ramen = shopItem('ramen', 'food', [-15, 25, 20], 10)
            self.foodInv[Ramen] = 0
            Yakult = shopItem('yakult', 'drink', [5, 10, 10], 5)
            self.drinkInv[Yakult] = 0
        
        self.shopRestock()
    
    def shopRestock(self):
        for inventoryType in self.inventory:
            for item in inventoryType:
                inventoryType[item] += 5

    def sell(self, item, num):
        if item.objType == 'food':
            if self.foodInv[item] > stockNum:
                return False
            else:
                self.foodInv[item] -= num

        if item.objType == 'drink':
            stockNum = self.drinkInv[item]
            if num > stockNum:
                return False
            else:
                self.drinkInv[item] -= num

        if item.objType == 'decor':
            stockNum = self.decorInv[item]
            if num > stockNum:
                return False
            else:
                self.decorInv[item] -= num

        return item.price 

class shopItem(object):
    def __init__(self, name, objType, stats, *args):
        self.name = name
        self.objType = objType
        self.healthEffect = stats[0]
        self.energyEffect = stats[1]
        self.happyEffect = stats[2]
        if len(args) > 0:
            self.price = args[0]

LaPrima = Shop('La Prima', 'coffee')
print('--------------------')
print(LaPrima.name)
print('----------')
for invType in LaPrima.inventory:
    for item in invType:
        print(f'{item.name} = {item.price} coins')
        print(f'health = {item.healthEffect}')
        print(f'energy = {item.energyEffect}')
        print(f'happiness = {item.happyEffect}')
        print('----------')

PandaMarket = Shop('Panda Market', 'asianGrocery')
print('--------------------')
print(PandaMarket.name)
print('----------')
for invType in PandaMarket.inventory:
    for item in invType:
        print(f'{item.name} = {item.price} coins')
        print(f'health = {item.healthEffect}')
        print(f'energy = {item.energyEffect}')
        print(f'happiness = {item.happyEffect}')
        print('----------')

Entropy = Shop('Entropy+', 'grocery')
print('--------------------')
print(Entropy.name)
print('----------')
for invType in Entropy.inventory:
    for item in invType:
        print(f'{item.name} = {item.price} coins')
        print(f'health = {item.healthEffect}')
        print(f'energy = {item.energyEffect}')
        print(f'happiness = {item.happyEffect}')
        print('----------')

DecorGalore = Shop('Decor Galore', 'decor')
print('--------------------')
print(DecorGalore.name)
print('----------')
for invType in DecorGalore.inventory:
    for item in invType:
        print(f'{item.name} = {item.price} coins')
        print(f'health = {item.healthEffect}')
        print(f'energy = {item.energyEffect}')
        print(f'happiness = {item.happyEffect}')
        print('----------')
