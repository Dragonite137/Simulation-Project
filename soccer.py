import runWorld as rw
import drawWorld as dw
import pygame as pg
from random import randint

name = "Click the Soccer Ball to Stop it from Going in the Goal"
width = 800
height = 800
rw.newDisplay(width, height, name)

myimage = dw.loadImage("soccer_ball_1.bmp")
goal = dw.loadImage("goal.bmp")

def updateDisplay(state):
    dw.fill(dw.white)
    dw.draw(goal, (0, 0, 0, 0))
    dw.draw(myimage, (state[0], state[1], state[2], state[3]))

def updateState(state):
    return(state[0]+state[2],state[1] + state[3],state[2], state[3])

def endState(state):
    if ((state[0] > width or state[0] < 0 or state[1] > height or state[1] < 0) or (state[2]==0 and state[3]==0)):
        return True
    else:
        return False

def handleEvent(state, event):
    p = pg.mouse.get_pos()
    if ((p[0]>=state[0] and p[0] <= (state[0] + 98)) and  ((p[1]>=state[1] and p[1] <= (state[1] + 100)))):
        return(state[0], state[1], 0, 0)
        
    else:
        return(state)
   
initState = (400, 700, randint(-2,2),randint(-10,-8))
frameRate = 60

rw.runWorld(initState, updateDisplay, updateState, handleEvent, endState, frameRate)
