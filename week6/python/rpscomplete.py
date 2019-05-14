from microbit import *
import random

rock = "29992:02920:00000:00000:00000"
paper = "09990:09990:00000:00000:00000"
scissors = "29200:02920:00000:00000:00000"


rps = [rock,paper,scissors]

def reverse(string):
    returnString = ""
    for i in range(len(string),1,-1):
        returnString += string[i-1]
    return returnString

def displayPlayer(number):
    return Image(reverse(rps[number]))

def displayEnemy(number):
    return Image(rps[number])

def showState(player,enemy):
    display.show(displayPlayer(player) + displayEnemy(enemy))

def winner(player,enemy):
    if (player == enemy + 1):
        return 1
    elif (enemy == player + 1):
        return -1
    elif (enemy == player):
        return 0
    elif (player + 2 == enemy):
        return 1
    else:
        return -1

def displayResult(player,enemy):
    for i in range(0,5):
        display.clear()
        newImage = displayPlayer(player).shift_left(4-i) + displayEnemy(enemy).shift_right(4-i)
        display.show(newImage)
        sleep(100)
    
    sleep(1000)

    if (winner(player,enemy) == 0):
        display.scroll("Tie!")
    elif (winner(player,enemy) == 1):
        display.scroll("You Win!")
    else:
        display.scroll("You lose :(")

def displayPlayerChoice(choice,direction):
    for i in range(0,5):
        display.clear()
        newImage = Image()
        if direction == -1:
            newImage = displayPlayer(choice).shift_left(4-i)
        else:
            newImage = displayPlayer(choice).shift_right(4-i)
        display.show(newImage)
        sleep(100)

def aiChoose():
    return random.randint(0,2)

#Don't worry about anything above the play function, unless you want to know how it all works

def play():
    choice = 0
    displayPlayerChoice(choice,1)
    '''We need to make the game run forever'''
    while True:
        if button_a.is_pressed() and button_b.is_pressed():
            '''Ask the AI what it would like to do (then place this in a variable) (hint: aiChoose() will generate the AI's choice)'''
            aiMove = aiChoose()

            '''Check who wins (hint: we just need to figure out how to use displayResult)'''
            displayResult(choice,aiMove)

            '''display the player's current choice again (hint: look above or below to see how this is done)'''
            displayPlayerChoice(choice,1)

        elif button_b.is_pressed():
            '''Change the player's choice, and make sure that it's <= 2 (hint: using modulus (%) is a good idea here)'''
            choice += 1
            choice = choice % 3
            displayPlayerChoice(choice,1)

play()