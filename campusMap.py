from campus import *
campusMap = [
    [None, None, None, None,    None,    None,    None,    None,    None,    None, None, None, None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None, None, None, None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None, None, None],
    [None, True, True, True,    True,    True,    True,    True,    True,    True, True, True, True,  True,  True,  True,  True,  True,  True,  True,  True,  True,  True,  True, True, True, True,   True,   True,   True,   True,   True,   True,   True,   True,   True,   True,   True, True, None],
    [None, True, None, None,    None,    None,    None,    None,    None,    None, True, None, None,  None,  None,  None,  None,  None,  True,  None,  None,  None,  None,  None, None, None, True,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None, True, None],
    [None, True, None, CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   None, True, None, Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt, Hunt, None, True,   None,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   None, True, None],
    [None, True, None, CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   None, True, None, Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt, Hunt, None, True,   None,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   None, True, None],
    [None, True, None, CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   None, True, None, Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt, Hunt, None, True,   None,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   None, True, None],
    [None, True, None, CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   None, True, None, Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt, Hunt, None, True,   None,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   None, True, None],
    [None, True, None, CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   None, True, None, Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt, Hunt, None, True,   None,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   None, True, None],
    [None, True, None, CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   None, True, None, Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt,  Hunt, Hunt, None, True,   None,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   None, True, None],
    [None, True, None, CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   None, True, None, None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None, None, None, True,   None,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   None, True, None],
    [None, True, None, CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   None, True, True, True,  True,  True,  True,  True,  True,  True,  True,  True,  True,  True,  True, True, True, True,   None,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   None, True, None],
    [None, True, True, CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   None, True, None, None,  None,  None,  None,  None,  None,  True,  None,  None,  None,  None,  None, None, None, True,   None,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   None, True, None],
    [None, True, None, CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   None, True, None, UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC, UniC, None, True,   None,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   None, True, None],
    [None, True, None, CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   None, True, None, UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC, UniC, None, True,   None,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   True, True, None],
    [None, True, None, CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   None, True, None, UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC, UniC, None, True,   None,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   None, True, None],
    [None, True, None, CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   None, True, None, UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC, UniC, None, True,   None,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   None, True, None],
    [None, True, None, CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   None, True, None, UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC, UniC, None, True,   None,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   None, True, None],
    [None, True, None, CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   None, True, None, UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC, UniC, None, True,   None,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   None, True, None],
    [None, True, None, CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   CFArt,   None, True, None, UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC, UniC, None, True,   None,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   None, True, None],
    [None, True, None, None,    None,    None,    None,    None,    None,    None, True, None, UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC, UniC, None, True,   None,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   None, True, None],
    [None, True, True, True,    True,    True,    True,    True,    True,    True, True, None, UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC,  UniC, UniC, None, True,   None,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   None, True, None],
    [None, True, None, None,    None,    None,    None,    None,    None,    None, True, None, None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None, None, None, True,   None,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   None, True, None],
    [None, True, None, Doherty, Doherty, Doherty, Doherty, Doherty, Doherty, None, True, True, True,  True,  True,  True,  True,  True,  True,  True,  True,  True,  True,  True, True, True, True,   None,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   Wean,   None, True, None],
    [None, True, None, Doherty, Doherty, Doherty, Doherty, Doherty, Doherty, None, True, None, None,  None,  None,  None,  None,  True,  None,  None,  None,  None,  None,  None, True, False, True,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None, True, None],
    [None, True, None, Doherty, Doherty, Doherty, Doherty, Doherty, Doherty, None, True, None, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, None, True, True, True,   True,   True,   True,   True,   True,   True,   True,   True,   True,   True,   True, True, None],
    [None, True, None, Doherty, Doherty, Doherty, Doherty, Doherty, Doherty, None, True, None, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, None, True, None, None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None, True, None],
    [None, True, None, Doherty, Doherty, Doherty, Doherty, Doherty, Doherty, None, True, None, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, None, True, None, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, None, True, None],
    [None, True, None, Doherty, Doherty, Doherty, Doherty, Doherty, Doherty, None, True, None, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, None, True, None, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, None, True, None],
    [None, True, None, Doherty, Doherty, Doherty, Doherty, Doherty, Doherty, None, True, None, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, None, True, None, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, None, True, None],
    [None, True, None, Doherty, Doherty, Doherty, Doherty, Doherty, Doherty, True, True, None, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, None, True, None, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, None, True, None],
    [None, True, None, Doherty, Doherty, Doherty, Doherty, Doherty, Doherty, None, True, None, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, None, True, None, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, None, True, None],
    [None, True, None, Doherty, Doherty, Doherty, Doherty, Doherty, Doherty, None, True, None, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, None, True, True, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, None, True, None],
    [None, True, None, Doherty, Doherty, Doherty, Doherty, Doherty, Doherty, None, True, None, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, None, True, None, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, None, True, None],
    [None, True, None, Doherty, Doherty, Doherty, Doherty, Doherty, Doherty, None, True, None, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, None, True, None, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, None, True, None],
    [None, True, None, Doherty, Doherty, Doherty, Doherty, Doherty, Doherty, None, True, None, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, None, True, None, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, None, True, None],
    [None, True, None, Doherty, Doherty, Doherty, Doherty, Doherty, Doherty, None, True, None, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, None, True, None, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, None, True, None],
    [None, True, None, Doherty, Doherty, Doherty, Doherty, Doherty, Doherty, None, True, None, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, Gates, None, True, None, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, Tepper, None, True, None],
    [None, True, None, None,    None,    None,    None,    None,    None,    None, True, None, None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None, True, None, None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None, True, None],
    [None, True, True, True,    True,    True,    True,    True,    True,    True, True, True, True,  True,  True,  True,  True,  True,  True,  True,  True,  True,  True,  True, True, True, True,   True,   True,   True,   True,   True,   True,   True,   True,   True,   True,   True, True, None],
    [None, None, None, None,    None,    None,    None,    None,    None,    None, None, None, None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None, None, None, None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None, None, None]
]

# # print(len(campusMap))
for i in range(len(campusMap)):
    # print(len(campusMap[i]))
    for j in range(len(campusMap[0])):
        if campusMap[i][j] == False:
            print((i,j))

# test cases/test maps
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
# startingNode=(5,10)
# # startingNode=(5,2)
# # endingNode=(5,2)
# endingNode=(17,5)

# # hardcoded test map #2
# campusMap=[
#     [None, None,  None,  None,  None,  None,  None,   None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None, None, None],
#     [None, True,  True,  True,  True,  True,  True,   True,  True,  True,  True,  True,  True,  True,  True,  True,  True,  True, True, None],
#     [None, True,  None,  None,  None,  None,  True,   None,  None,  None,  None,  True,  None,  True,  None,  None,  None,  None, True, None],
#     [None, True,  None,  False, False, None,  True,   None,  False, False, None,  True,  None,  True,  None,  False, False, None, True, None],
#     [None, True,  None,  False, False, None,  True,   None,  False, False, None,  True,  True,  True,  None,  False, False, None, True, None],
#     [None, True,  True,  False, False, None,  True,   None,  False, False, True,  True,  None,  True,  None,  False, False, None, True, None],
#     [None, True,  None,  False, False, None,  True,   None,  False, False, None,  True,  None,  True,  None,  False, False, None, True, None],
#     [None, True,  None,  False, False, None,  True,   None,  False, False, None,  True,  None,  True,  None,  False, False, True, True, None],
#     [None, True,  None,  False, False, None,  True,   None,  False, False, None,  True,  None,  True,  None,  False, False, None, True, None],
#     [None, True,  None,  None,  None,  None,  True,   None,  None,  None,  None,  True,  None,  True,  None,  False, False, None, True, None],
#     [None, True,  True,  True,  True,  True,  True,   True,  True,  True,  True,  True,  True,  True,  None,  None,  None,  None, True, None],
#     [None, True,  None,  None,  None,  None,  None,   None,  True,  None,  None,  None,  None,  True,  True,  True,  True,  True, True, None],
#     [None, True,  None,  False, False, False, False,  None,  True,  None,  False, False, None,  True,  None,  None,  True,  None, True, None],
#     [None, True,  None,  False, False, False, False,  None,  True,  None,  False, False, None,  True,  None,  False, False, None, True, None],
#     [None, True,  None,  False, False, False, False,  None,  True,  None,  False, False, None,  True,  None,  False, False, None, True, None],
#     [None, True,  None,  False, False, False, False,  None,  True,  None,  False, False, None,  True,  None,  False, False, None, True, None],
#     [None, True,  None,  False, False, False, False,  None,  True,  None,  False, False, None,  True,  None,  False, False, None, True, None],
#     [None, True,  None,  None,  None,  True,  None,   None,  True,  None,  None,  True,  None,  True,  None,  None,  None,  None, True, None],
#     [None, True,  True,  True,  True,  True,  True,   True,  True,  True,  True,  True,  True,  True,  True,  True,  True,  True, True, None],
#     [None, None,  None,  None,  None,  None,  None,   None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None, None, None]
# ]

# print(pathfinder(campusMap, startingNode, endingNode))