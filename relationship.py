# Relationships

class OtherPerson(object):
    def __init__(self, name, personType):
        self.personType = personType
        self.rLevel = 30

    def levelCap(self):
        if self.rLevel < 0:
            self.rLevel = 0
        elif self.rLevel > 100:
            self.rLevel = 100

    def bribe(self, item):
        if ((self.personType == 'TA' or self.personType == 'prof') 
             and (self.rLevel >= 70)):
            if item.type == 'drink' or item.type == 'food':
                self.rLevel += 5
                self.levelCap()
                return True
            else:
                return None
        else:
            if ((self.personType == 'TA' or self.personType == 'prof')):
                self.rLevel = 0
            self.levelCap()
            return False
    
    def chat(self, topic):
        if topic.type == False:
            self.rLevel -= 15
        elif topic.type == True:
            self.rLevel += 10
        self.levelCap()
    
    def hangout(self):
        if self.personType == 'friend': 
            self.rLevel += 20
            self.levelCap()
            return True
        else:
            return False

# friends
Mia = OtherPerson('Mia', 'friend')
Amira = OtherPerson('Amira', 'friend')
Tiffany = OtherPerson('Tiffany', 'friend')


# TAs
Lauren = OtherPerson('Lauren', 'TA')
Melinda = OtherPerson('Melinda', 'TA')


# professors
# Austin = OtherPerson('Austin', 'prof')

BizProf1 = OtherPerson('McEcon', 'prof')
BizProf2 = OtherPerson('Managier', 'prof')
BizProf3 = OtherPerson('Ah Kow Ting', 'prof')

ArtProf1 = OtherPerson('Schetch', 'prof')
ArtProf2 = OtherPerson('Panetin', 'prof')
ArtProf3 = OtherPerson('Art Teori', 'prof')

MathProf1 = OtherPerson('Cakulas', 'prof')
MathProf2 = OtherPerson('Nume Bers', 'prof')
MathProf3 = OtherPerson('Al Jeba', 'prof')

SciProf1 = OtherPerson('Bye-o', 'prof')
SciProf2 = OtherPerson('Kemistre', 'prof')
SciProf3 = OtherPerson('Fisacs', 'prof')

EngProf1 = OtherPerson('Poe Atree','prof')
EngProf2 = OtherPerson('Gramer','prof')
EngProf3 = OtherPerson('Ese','prof')

HistProf1 = OtherPerson('Laydee','prof')
HistProf2 = OtherPerson('Qin','prof')
HistProf3 = OtherPerson('Artisteori','prof')

CSProf1 = OtherPerson('Taykoschick','prof')
CSProf2 = OtherPerson('Al Goritim','prof')
CSProf3 = OtherPerson('Daytha','prof')
