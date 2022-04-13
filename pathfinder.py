# This is my Pathfinder!

# Node class to help store info about each node
class Node(object):
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.parent = parent

    def __eq__(self, other):
        if ((self.x == other.x) and (self.y == other.y)):
            return True
        return False

# distance heuristic, specifically the Manhattan distance heuristic
# Manhattan heuristic utilized specifically because my game 
# only allows for 4 directions of movement (up, down, left, right)
def distHeuristic(startX, startY, endX, endY):
    return abs((startX-endX))+abs((startY-endY))

# Citations & Sources!
# pathfinder function and Node class written with 
# help from the following sources:
# ----------------------------------------------------
# section titled 'Algorithm'
# https://www.pythonpool.com/a-star-algorithm-python/
# ----------------------------------------------------
# section titled 'A* Pseudocode'
# https://stackabuse.com/graphs-in-java-a-star-algorithm/
# ----------------------------------------------------
# sections titled 'F=G+H', 'Pseudocode'
# note #1: in 'Pseudocode' section, only loosely based off provided template
# (some key differences)
# note #2:
# only referenced Node class and initializing of startNode and goalNode 
# from Source Code section
# https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
# ----------------------------------------------------
# sections titled 'Heuristics' and 'The A* Algorithm'
# https://brilliant.org/wiki/a-star-search/#:~:text=The%20pseudocode%20for%20
# the%20A,presented%20with%20Python%2Dlike%20syntax.&text=The%20time%20complex
# ity%20of%20A,search%20space%20is%20a%20tree
# ----------------------------------------------------
# section titled 'Heuristics for grid maps'
# http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html

# pathfinding function utilizing the A* algorithm
def pathfinder(map, startingNode, endingNode):
    openList = []
    closedList = []

    # initialize start and goal nodes
    startNode = Node(startingNode[0], startingNode[1], None)
    startNode.f = startNode.g = startNode.h = 0
    goalNode = Node(endingNode[0], endingNode[1], None)
    goalNode.f = goalNode.g = goalNode.h = 0

    openList.append(startNode)

    while len(openList) > 0:
        print('------------------------------')
        openNodesOutput = []
        for openNode in openList:
            openNodesOutput.append((openNode.x, openNode.y))
        print(f'current openList = {openNodesOutput}')

        # find the open node with the lowest f(n)
        currNode = openList[0]
        currIndex = 0
        for i in range(1, len(openList)):
            if (currNode.f > openList[i].f):
                currNode = openList[i]
                currIndex = i

        print(f'currNode = ({currNode.x}, {currNode.y}), currIndex = {currIndex}')

        # solution found!
        if currNode == goalNode:
            print('solution found!!!')
            return getPath(currNode, startNode, [])

        openList.pop(currIndex)
    
        # possible moves
        moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]

        # go through possible child/neighbor nodes of the 'best' currNode
        childNodes = []
        for move in moves:
            newX = currNode.x + move[0]
            newY = currNode.y + move[1]

            print(f'newX = {newX}, newY = {newY}')

            # check if newX, newY is valid before making Node(for efficiency)
            if isValid(newX, newY, campusMap):
                print('newX and newY were valid!')
                childNode = Node(newX, newY, currNode)
                childNodes.append(childNode)

        childNodesOutput = []
        for child in childNodes:
            childNodesOutput.append((child.x, child.y))
        print(f'childNodes = {childNodesOutput}')
        # go through child nodes and add them to openList to be 'analyzed'
        for child in childNodes:
            if ((child not in openList) and (child not in closedList)):
                child.g = currNode.g + 1
                child.h = distHeuristic(child.x, child.y, 
                                        goalNode.x, goalNode.y)
                child.f = child.g + child.h
                openList.append(child)
        
        openNodesOutput = []
        for openNode in openList:
            openNodesOutput.append((openNode.x, openNode.y))
        print(f'new openList = {openNodesOutput}')

        
        # already analyzed currNode, scheduled neighbors
        closedList.append(currNode)

# helper function to return nicely formatted path output
def getPath(node, startNode, path):
    if node == startNode:
        path.append((node.x, node.y))
        return path[::-1]
    else:
        path.append((node.x, node.y))
        return getPath(node.parent, startNode, path)

# helper function to check boundaries and 'walkability' of given node
def isValid(x, y, map):
    if (0<=x<len(map)) and (0<=y<len(map[0]) 
        and (map[x][y] == True)):
        return True
    return False

# test cases
# startingNode=(2,4)
# endingNode=(7,3)
# endingNode=(7,3)
# endingNode=(7,6)

# None = grass
# False = building
# True = road

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

# test starting and ending nodes
startingNode=(5,10)
# startingNode=(5,2)
# endingNode=(5,2)
endingNode=(17,5)

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

print(pathfinder(campusMap, startingNode, endingNode))