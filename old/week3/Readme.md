# Week 3 - Programming!

This week, we're going to get a game working!

## Let's play the game first

First, let's see what the game even is - download the hex file, and let's see: [hex file](Completed/tiltball.hex?raw=true)

To run that on your Microbit, just copy it onto the microbit.

## Now, let's program it

We have a copy of the game from just before it was finished - [tiltball.py](Python%20Files/tiltball.py?raw=true). Let's download that and have a look at it.

```python
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
```

There's quite a lot of code there, huh.

To make the game work, we're going to have to write a fair amount of code, and we'll go through that in a minute, but first, we need to go through a number of things in Python.

### Functions and Variables

#### Functions
Functions allow us to get a block of code, and run it again, without needing to copy-paste the code. In Python, we write a function as follows:
```py
def functionName(<arguments>):
    '''code inside function goes here'''
```
That should probably look familiar, but let's look at what the `<arguments>` part is.

An argument is something that we pass into a function. Say we have the function below:

```py
def sum():
    return 1 + 2
```

And to get the result, we go like this:

```py
sum() #3
```

Well, that function will always return 3. That's great if we always want our sum to be 3, but what about if we want to be able to use it for more than 1 + 2?

This is what arguments are for - here's another function:

```py
def sum(a,b):
    return a + b
```

Because we are using arguments here, the function needs to be accessed like this:
```py
sum(1,2) #3
```

This is great though - we can now get the sum of any two numbers by calling our function like that.

The other important thing about functions, is that if they return, they are the same as just writing their response; that is to say:

```py
sum(1,sum(1,2))
```

will give 4, because first, we find that `sum(1,2)` is 3, and then calculate `sum(1,3)`, to get 4.

#### Variables
Variables are like functions - they make programming easier by allowing us to store something and do things to it. For example, say we want to write a function that will take a number and add 5 to it, then multiply it by half of itself plus 1:

without variables, we would have to do it like this:
```py
def doAThing(n):
    return (n + 1) * ((n + 1) / 2)
```
but with variables, we can do this:
```py
def doAThing(n):
    x = n + 1
    return x * (x / 2)
```
The second one is a lot more easy to read, and we can use variables for much more complicated stuff too. If we wanted to edit an image that will display on the microbit, for example, we could do it like this:
```py
Image.HAPPY.set_pixel(0,0,9).set_pixel(1,0,9).set_pixel(2,0,9)
```
or with variables (and a loop):
```py
img = Image.HAPPY
for i in range(0,2): #'i' will start at 0, then become 1, then become 2, and the code below will run each time
    img.set_pixel(i,0,9)
```

### Making the game work

There's a few functions we will have to edit: `chooseGoal`, `placePlayer`, `getDirection`, `moveTheBall` and `runGame`.

We will go through one fix here, then you try with the others - and don't forget to ask for help if you need it.

We're going to do one of the things in `runGame`:

Below line `149`, we need to display the image on the screen, as is explained by the comment.
```py
'''we need to dim the image as the time runs out, then show it on the display'''
```

The variable `frame` already seems like it's storing an image, so let's try that, by adding:

`display.show(frame)`

So now, let's build to our microbit.

When the text finishes scrolling, press either button, and you should see something on the display. That's great - it's starting to work!

We only have to dim the display, but we'll come back to that after fixing the other things first. Below are a few hints:

### Hints

#### Getting a random number (chooseGoal)

Here, we need to choose two random numbers: one between `minx` and `maxx`, and another between `miny` and `maxy`.

Take a look at how we get random numbers in `placePlayer` to try to figure out how to do this, and set the results to the variables x and y.

#### Placing the ball somewhere (placePlayer)

To place the ball somewhere, we can just set its coordinates:

To set the `x` coordinate, we can use `ballLocation[0] = <some number>`.

Similarly, to set the `y` coordinate, we can use `ballLocation[1] = <some number>`.

#### Moving the ball (moveTheBall)

We need to check whether the new location is somewhere the ball can be - remember, the ball can only be at a location marked with `0 (nothing)` or `3 (the goal)`. Another way of saying this, is that the ball cannot be at a location marked with `1 (wall)`.

To get the marking of a location, we can use `theMap[x][y]`, and to get the x and y values of `newLocation`, we can use `newLocation[0]` for `x`, and `newLocation[1]` for `y`.

#### Dimming the display (runGame) [Most complicated]

`*` can be used to multiply all the pixels shown on the display by a given number.

If we multiply all the pixels by a number that is less than one, it should get dimmer, but we need this to be based on how much time we have left.

Try to figure out a way of making a number that is less than one, and goes down as the variable "`ticks`" goes up.

The number of ticks until you lose the game is: `max(allowedTicks,minimumAllowedTicks)`. You will need to use this somewhere.

## If you finish all that, please let me know. Otherwise, ask for help if you need it.

## Extension
If you haven't completed last week's extension, you can do that [Last Week](../week2/Readme.md#part-4---extension)

If you have done that, please let me know.