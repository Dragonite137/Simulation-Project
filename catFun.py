import runWorld as rw
import drawWorld as dw
import pygame as pg
from random import randint

# Initialize world
name = "Cat Spiral"
width = 800
height = 800
rw.newDisplay(width, height, name)

myimage = dw.loadImage("cat.bmp")

def updateDisplay(state):
    dw.fill(dw.white)
    dw.draw(myimage, (state[0], state[1],state[2]))

# state -> state
def updateState(state):
    def spiral(n, angle, step):
        for step in range(n):
            forward(step)
            left (angle)
    spiral(140,61,10)
    state = spiral
    return(state)

# state -> bool
def endState(state):
    if (state[0] > width or state[0] < 0 or state[1] > height or state[1] < 0):
        return True
    else:
        return False

# state -> event -> state
def handleEvent(state, event):  

    if (event.type == pg.MOUSEBUTTONDOWN):
        return(state[0],state[1],randint(-5,5),randint(-5,5))
    else:
        return(state)

initState = (400, 400)

frameRate = 60

rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
