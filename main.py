from cmu_cs3_graphics import *
import copy
from pathfinder import pathfinder

# hardcoded test map #1
# campusMap=[
#     [None, None,  None,  None,  None, None, None, None,  None,  None],
#     [None, False, False, False, None, None, None, False, False, None],
#     [None, False, False, False, True, True, True, False, False, None],
#     [None, False, False, False, None, True, None, False, False, None],
#     [None, False, False, False, None, True, None, None,  None,  None],
#     [None, None,  None,  None,  None, True, None, False, False, None],
#     [None, False, False, None,  None, True, None, False, False, None],
#     [None, False, False, True,  True, True, True, False, False, None],
#     [None, False, False, None,  None, None, None, False, False, None],
#     [None, None,  None,  None,  None, None, None, None,  None,  None]
# ]

# hardcoded test map #2
campusMap=[
    [None, None,  None,  None,  None,  None,  None,   None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None, None, None],
    [None, True,  True,  True,  True,  True,  True,   True,  True,  True,  True,  True,  True,  True,  True,  True,  True,  True, True, None],
    [None, True,  None,  None,  None,  None,  True,   None,  None,  None,  None,  True,  None,  True,  None,  None,  None,  None, True, None],
    [None, True,  None,  False, False, None,  True,   None,  False, False, None,  True,  None,  True,  None,  False, False, None, True, None],
    [None, True,  None,  False, False, None,  True,   None,  False, False, None,  True,  True,  True,  None,  False, False, None, True, None],
    [None, True,  True,  False, False, None,  True,   None,  False, False, True,  True,  None,  True,  None,  False, False, None, True, None],
    [None, True,  None,  False, False, None,  True,   None,  False, False, None,  True,  None,  True,  None,  False, False, None, True, None],
    [None, True,  None,  False, False, None,  True,   None,  False, False, None,  True,  None,  True,  None,  False, False, True, True, None],
    [None, True,  None,  False, False, None,  True,   None,  False, False, None,  True,  None,  True,  None,  False, False, None, True, None],
    [None, True,  None,  None,  None,  None,  True,   None,  None,  None,  None,  True,  None,  True,  None,  False, False, None, True, None],
    [None, True,  True,  True,  True,  True,  True,   True,  True,  True,  True,  True,  True,  True,  None,  None,  None,  None, True, None],
    [None, True,  None,  None,  None,  None,  None,   None,  True,  None,  None,  None,  None,  True,  True,  True,  True,  True, True, None],
    [None, True,  None,  False, False, False, False,  None,  True,  None,  False, False, None,  True,  None,  None,  True,  None, True, None],
    [None, True,  None,  False, False, False, False,  None,  True,  None,  False, False, None,  True,  None,  False, False, None, True, None],
    [None, True,  None,  False, False, False, False,  None,  True,  None,  False, False, None,  True,  None,  False, False, None, True, None],
    [None, True,  None,  False, False, False, False,  None,  True,  None,  False, False, None,  True,  None,  False, False, None, True, None],
    [None, True,  None,  False, False, False, False,  None,  True,  None,  False, False, None,  True,  None,  False, False, None, True, None],
    [None, True,  None,  None,  None,  True,  None,   None,  True,  None,  None,  True,  None,  True,  None,  None,  None,  None, True, None],
    [None, True,  True,  True,  True,  True,  True,   True,  True,  True,  True,  True,  True,  True,  True,  True,  True,  True, True, None],
    [None, None,  None,  None,  None,  None,  None,   None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None, None, None]
]

class Student(object):
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.andrewID = firstName + lastName[0]
        self.health = 100
        self.happiness = 100
        self.energy = 100

class Building(object):
    buildings = []
    def __init__(self, name, color, size, x, y):
        Building.buildings.append(self)
        self.name = name
        self.color = color
        self.size = size
        self.x = x
        self.y = y

# wean=Building('wean', 'tan', 100, 50, 25)
# doherty=Building('doherty', 'green', 100, 200, 25)
# gates=Building('gates', 'gray', 100, 350, 25)
# baker=Building('baker', 'yellow', 100, 50, 275)
# cfa=Building('cfa', 'pink', 100, 200, 275)
# cm=Building('cm', 'purple', 100, 350, 275)

class Lecture(object):
    def __init__(self, courseName):
        self.courseName = courseName

# test starting and ending nodes
startingNode=(7,17)
destinationNode=(5,2)
print(pathfinder(campusMap, startingNode, destinationNode))

def redrawAll(app):
    # draws campusMap with piece type and coordinates
    for i in range(len(campusMap)):
        for j in range(len(campusMap[0])):
            x=50*j + 50
            y=50*i + 50
            if campusMap[i][j] == None:
                drawRect(x, y, 50, 50, fill = 'green')
                drawLabel(f'g ({i},{j})', x+25, y+25, size=9.5)
            elif campusMap[i][j] == False:
                drawRect(x, y, 50, 50, fill = 'brown')
                drawLabel(f'b ({i},{j})', x+25, y+25, size=9.5)
            elif campusMap[i][j] == True:
                drawRect(x, y, 50, 50, fill = 'gray')
                drawLabel(f'r ({i},{j})', x+25, y+25, size=9.5)
    pass

def main():
    runApp(1100, 1100)

main()
# katelyn=Student('katelyn', 'zheng')
# print(katelyn.andrewID)

# mia=Student('mia', 'evans')
# print(mia.andrewID)

# prettyPrint(campusMap)

# buildingsLocation = [(50, 50), (100, 50)]
# buildingsSize=[(25, 25), (25, 25)]
# # print(Building.buildings[1].name)
