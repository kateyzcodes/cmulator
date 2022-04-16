from cmu_cs3_graphics import *
from pathfinder import *
from campus import *
# from grades import *
# from relationship import *
# from shops import *
# from utilityf import *
from campusMap import *

# jazzyTrack = Sound('C:\Users\katel\Downloads\[MP3FY] JAZZ (full EP).mp3')
# jazzyTrack.play()
def onAppStart(app):
    
    app.campusMap = campusMap

    app.rows = len(app.campusMap)
    app.cols = len(app.campusMap[0])
    app.studentRow = campusStart.x
    app.studentCol = campusStart.y
    app.destRow = campusStart.x
    app.destCol = campusStart.y
    app.currSpriteIndex = 0
    # app.walkingX, app.walkingY = 250, 230
    app.walking1URL = 'https://i.imgur.com/f4Y3bYO.png'
    app.walking2URL = 'https://i.imgur.com/4pNg01W.png'
    app.walking3URL = 'https://i.imgur.com/x4owlk2.png'   
    app.sprites = [app.walking1URL, app.walking2URL, app.walking3URL]
    app.autowalk = False
    app.path = pathfinder(app.campusMap, (app.studentRow, app.studentCol), (app.destRow, app.destCol))

    # app.studentColor = 'purple'

    app.stepsPerSecond = 10
    
def onStep(app):
    if app.autowalk == True:
        if len(app.path) > 0:
            doStep(app)
    
def doStep(app):
    app.studentRow, app.studentCol = app.path[0]
    if app.currSpriteIndex == 2:
       app.currSpriteIndex = 0
    else:
        app.currSpriteIndex += 1
    if app.destRow == app.studentRow and app.destCol == app.studentCol:
        app.currSpriteIndex = 0
    app.path = app.path[1:]

def onMousePress(app, mouseX, mouseY):
    print('clicked...')
    mouseRow = int(mouseY / (len(campusMap[0])//4))
    mouseCol = int(mouseX / (len(campusMap)//4))
    print(f'mouseX = {mouseX}, mouseY = {mouseY}')
    print(f'mouseRow = {mouseRow}, mouseCol = {mouseCol}')
    if 0<=mouseRow<app.rows and 0<=mouseCol<app.cols:
        if isinstance(app.campusMap[mouseRow][mouseCol], Building):
            print('passed checks')
            app.destRow = campusMap[mouseRow][mouseCol].entranceRow
            app.destCol = campusMap[mouseRow][mouseCol].entranceCol
            app.path = pathfinder(app.campusMap, (app.studentRow, app.studentCol), (app.destRow, app.destCol))
            app.autowalk = True

def onKeyPress(app, key):
    if app.autowalk == True:
        return
    if key == 'left':
        app.studentCol -= 1
        if (app.studentCol < 0 or app.studentCol > (len(app.campusMap[0])-1)):
            app.studentCol += 1
        elif (app.campusMap[app.studentRow][app.studentCol]!=True):
            app.studentCol += 1
    elif key == 'right':
        app.studentCol += 1
        if (app.studentCol < 0 or app.studentCol > (len(app.campusMap[0])-1)):
            app.studentCol -= 1
        elif (app.campusMap[app.studentRow][app.studentCol]!=True):
            app.studentCol -= 1
    elif key == 'up':
        app.studentRow -= 1
        if (app.studentRow < 0 or app.studentRow > (len(app.campusMap)-1)):
            app.studentRow += 1
        elif (app.campusMap[app.studentRow][app.studentCol]!=True and app.campusMap[app.studentRow][app.studentCol]!=False):
            app.studentRow += 1
    elif key == 'down':
        app.studentRow += 1
        if (app.studentRow < 0 or app.studentRow > (len(app.campusMap)-1)):
            app.studentRow -= 1
        elif (app.campusMap[app.studentRow][app.studentCol]!=True):
            app.studentRow -= 1

def drawStudent(app):
    x, y, width, height = getCellBounds(app, app.studentRow, app.studentCol)
    reverseImg = False
    if app.destCol<app.destRow:
        reverseImg = True
    drawImage(app.sprites[app.currSpriteIndex], x-5, y-10, width = 20, height = 20)

    # drawRect(x, y, width, height, fill = app.studentColor)
    

def getCellBounds(app, row, col):
    cellWidth=(app.width)/app.cols
    cellHeight=(app.height)/app.rows
    left=cellWidth*col
    top=cellHeight*row
    return left, top, cellWidth, cellHeight

def redrawAll(app):
    # draws campusMap with piece type and coordinates
    for i in range(len(app.campusMap)):
        for j in range(len(app.campusMap[0])):
            # # x=50*j + 50
            # # y=50*i + 50
            # x = 50*j
            # y = 50*i
            x, y, width, height = getCellBounds(app, i, j)
            # print((width, height))
            if app.campusMap[i][j] == None:
                drawRect(x, y, width, height, fill = 'green')
                # drawLabel(f'g ({i},{j})', x+width/2, y+height/2, size=5)
            elif app.campusMap[i][j] == False:
                drawRect(x, y, width, height, fill = 'yellow')
                # drawLabel(f's ({i},{j})', x+width/2, y+height/2, size=5)
            elif isinstance(app.campusMap[i][j], Building):
                drawRect(x, y, width, height, fill = 'red')
                # drawLabel(f'b ({i},{j})', x+width/2, y+height/2, size=5)
            elif app.campusMap[i][j] == True:
                drawRect(x, y, width, height, fill = 'gray')
                # drawLabel(f'r ({i},{j})', x+width/2, y+height/2, size=5)
    drawStudent(app)

def main():
    runApp(400, 400)
    # runApp(1100, 1100)

main()