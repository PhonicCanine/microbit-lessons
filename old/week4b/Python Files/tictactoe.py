import random

board = [["1","2","3"],
         ["4","5","6"],
         ["7","8","9"]]

def initialiseBoard():
    global board
    board = [["1","2","3"],
             ["4","5","6"],
             ["7","8","9"]]

def getPos(y,x):
    global board

    '''We need to return whatever is at the board position x,y'''
    

def setPos(y,x,value):
    global board

    '''We need to set the board position at x,y to the value we have passed in'''
    

#
#
# Only look at the code below here if you are interested!
# If you just want to get the game working, you only have to write the code above
#
#


def displayBoard():
    global board

    #Loop through each row of the board, and display it
    for y in range(0,3):
        print (board[y])

def checkForWin():
    hasWon = False
    #First check for 3 across
    for y in range(0,3):
        same = True
        for x in range(0,3):
            if x > 0:
                same = same and getPos(y,(x-1)) == getPos(y,x)
        if (same):
            hasWon = True
    #Then check for 3 down
    for x in range(0,3):
        same = True
        for y in range(0,3):
            if y > 0:
                same = same and getPos((y-1),x) == getPos(y,x)
        if (same):
            hasWon = True
    #Finally check diagonals
    hasWon = hasWon or (getPos(0,0) == getPos(1,1) and getPos(1,1) == getPos(2,2)) or (getPos(0,2) == getPos(1,1) and getPos(1,1) == getPos(2,0))
    return hasWon


running = True
while running:
    wouldYouLikeToPlay = input("Would you like to play a game? (Y/n)")
    if wouldYouLikeToPlay == "" or wouldYouLikeToPlay.lower().startswith("y"):
        gameWon = False

        #Clear the board
        initialiseBoard()
        print("You are going to play as O, so the computer will move first")

        #Place the computer's first piece
        setPos(random.randint(0,2),random.randint(0,2),"X")

        #Loop while the game has not been won
        while not gameWon:

            #Display the board
            displayBoard()

            #Get the players input
            playerChoice = input("Where would you like to place a piece?")
            playHappened = False
            for y in range(0,3):
                for x in range(0,3):

                    #If this coordinate is the number that the player entered (and they didn't try to cheat by using "X" or "O")
                    if getPos(y,x) == playerChoice and (playerChoice != "X" and playerChoice != "O"):

                        #Confirm that something has happened this turn, and set the board position to an O
                        playHappened = True
                        setPos(y,x,"O")

                        #If there has been a win since that piece was placed, the player has won, so tell them that
                        if checkForWin():
                            print("You won!")
                            displayBoard()
                            gameWon = True
                        
                        #Otherwise, we need to see what the computer will do
                        else:
                            nextPosX = random.randint(0,2)
                            nextPosY = random.randint(0,2)

                            #Generate new random numbers until the computer has selected an empty square
                            while getPos(nextPosY,nextPosX) == "X" or getPos(nextPosY,nextPosX) == "O":
                                nextPosX = random.randint(0,2)
                                nextPosY = random.randint(0,2)

                            #Place an X in the square that the computer has chosen
                            setPos(nextPosY,nextPosX,"X")

                            #If there has been a win after that piece was placed, the computer has won, so say that
                            if checkForWin():
                                print("Computer won!")
                                displayBoard()
                                gameWon = True

            #If nothing happened this turn, it means the player chose an invalid space, so tell them that
            if not playHappened:
                print("Please choose an unoccupied space")

            #Otherwise, we need to check if there are any free spaces
            else:
                vacantSquare = False
                for y in range(0,3):
                    for x in range(0,3):
                        #This line is a bit complicated, but, basically, if there is any unfilled square, this will set vacantSquare to True. If you've got any questions about this, I can explain it to you in more detail.
                        vacantSquare = vacantSquare or (getPos(y,x) != "X" and getPos(y,x) != "O")

                #If there are no blank spaces, and the game hasn't been won, then there has been a draw.
                if not vacantSquare and not gameWon:
                    gameWon = True
                    print("It was a draw!")
                    displayBoard()