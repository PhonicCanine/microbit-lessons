from microbit import *
import random

img = Image()
ballLocation = (5,5)
mapTL = (0,0)
mapBR = (10,10)
theMap = []

#Initialise the map
def init_map():
    global theMap
    theMap = []
    for x in range(mapBR[0] - mapTL[0]):
        theMap.append([])
        for y in range(mapBR[1] - mapTL[1]):
            if x == 0 or x == mapBR[0] - 1 or y == 0 or y == mapBR[1] - 1:
                theMap[x].append(1)
            else:
                theMap[x].append(0)

#Returns an image that represents the map
def img_dis():
    global theMap
    global ballLocation
    theImg = Image()
    imgx = 0
    imgy = 0
    for x in range(ballLocation[0] - 2,ballLocation[0] + 3):
        imgy = 0
        for y in range(ballLocation[1] - 2,ballLocation[1] + 3):
            if (x >= 0 and x < mapBR[0]) and (y >= 0 and y < mapBR[1]):
                if (theMap[x][y] == 1):
                    theImg.set_pixel(imgx,imgy,9)
                elif (theMap[x][y] == 0):
                    theImg.set_pixel(imgx,imgy,0)
                elif (theMap[x][y] == 3):
                    theImg.set_pixel(imgx,imgy,1)
            else:
                theImg.set_pixel(imgx,imgy,4)
            
            if (x == ballLocation[0] and y == ballLocation[1]):
                theImg.set_pixel(imgx,imgy,3)
            imgy = imgy + 1
        imgx = imgx + 1
    return theImg

#put the goal onto the map
def placeGoal(location):
    global theMap
    theMap[location[0]][location[1]] = 3
    theMap[location[0] + 1][location[1] + 1] = 3
    theMap[location[0] - 1][location[1] + 1] = 3
    theMap[location[0] + 1][location[1] - 1] = 3
    theMap[location[0] - 1][location[1] - 1] = 3
    theMap[location[0]][location[1] + 1] = 3
    theMap[location[0]][location[1] - 1] = 3
    theMap[location[0] + 1][location[1]] = 3
    theMap[location[0] - 1][location[1]] = 3


#Figure out where to place the goal
def chooseGoal():
    global mapTL
    global mapBR

    minx = mapTL[0] + 2
    maxx = mapBR[0] - 3

    miny = mapTL[1] + 2
    maxy = mapBR[1] - 3

    '''We need to get some number somehow (instead of just 3)'''

    x = 3
    y = 3

    placeGoal((x,y))

#Figure out where to put the ball
def placePlayer():
    global mapTL
    global mapBR
    global ballLocation

    x = random.randint(mapTL[0] + 1,mapBR[0] - 2)
    y = random.randint(mapTL[1] + 1,mapBR[1] - 2)

    '''we need to put the ball in our random location somehow'''

#Returns a vector (A tuple of two integers), describing the direction that the board is being leaned
def getDirection():
    '''we need to get the accelerometer values somehow (replace (0,0,0))'''
    accel = (0,0,0)
    return normaliseVector(accel)
    
#Each of these numbers will be between -1024 and 1023
def normaliseVector(vector3):
    x = vector3[0]
    y = vector3[1]
    z = vector3[2]
    retx = 0
    if (x > 256):
        retx = 1
    elif (x < -256):
        retx = -1
    
    rety = 0
    if (y > 256):
        rety = 1
    elif (y < -256):
        rety = -1
    
    return (retx,rety)

def moveTheBall():
    global ballLocation
    theLeanDirection = getDirection()
    newLocation = (ballLocation[0] + theLeanDirection[0], ballLocation[1] + theLeanDirection[1])
    '''we need to move the ball, if it's not going to be inside a wall, and set ballLocation to our newLocation'''

def runGame():
    global theMap
    display.scroll("Press any button to start!")
    while True:
        
        if button_a.is_pressed() or button_b.is_pressed():

            lostGame = False
            allowedTicks = 1000
            minimumAllowedTicks = 50
            tick = 0
            gameWon = False
            level = 0

            while not lostGame:

                #clear the map and setup game
                level = level + 1
                tick = 0
                init_map()
                placePlayer()
                chooseGoal()
                gameWon = False

                while tick < max(allowedTicks,minimumAllowedTicks) and not gameWon:
                    frame = img_dis()

                    '''we need to dim the image as the time runs out, then show it on the display'''

                    #move the ball, and sleep
                    moveTheBall()
                    sleep(100)
                    tick = tick + 1

                    '''figure out if the player has won (ball is in a space with a 3), and do something! (but make sure to set gameWon to True)'''
                if (tick >= allowedTicks and not gameWon):
                    display.show(Image.SAD)
                    sleep(1000)
                    display.scroll("You got to level: " + str(level))
                    runGame()
                elif gameWon:
                    allowedTicks = allowedTicks - 50
    
runGame()