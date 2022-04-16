from student import *

class Wallet(object):
    def __init__(self, person, rich):
        self.person = person
        self.rich = rich
        if self.rich == True:
            self.coins = 300
        else:
            self.coins = 100
    
    def checkBalance(self):
        return self.coins

    def deposit(self, amount):
        self.coins += amount

    def purchase(self, amount):
        if self.coins - amount >= 0:
            self.coins -= amount
            return True
        return False
        
    def donate(self, donator, receiver, amount):
        if receiver == 'CMU':
            if self.coins-amount >= 0:
                donator.happiness += 10
                self.coins -= amount
                return True
        elif receiver == 'charity':
            if self.coins-amount >= 0:
                donator.happiness += 25
                self.coins -= amount
                return True
        return False
