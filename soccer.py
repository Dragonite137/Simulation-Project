import runWorld as rw
import drawWorld as dw
import pygame as pg
from random import randint

name = "Soccer Game"
width = 800
height = 800
rw.newDisplay(width, height, name)

myimage = dw.loadImage("soccer_ball_1.bmp")
goal = dw.loadImage("goal.bmp")

def updateDisplay(state):
    dw.fill(dw.white)
    dw.draw(myimage, (state[0], state[1], state[2], state[3]))
    dw.draw(goal, (0, 0, 0, 0))

def updateState(state):
    return(state[0]+state[2],state[1] + state[3],state[2], state[3])

def endState(state):
    if (state[0] > width or state[0] < 0 or state[1] > height or state[1] < 0):
        return True
    else:
        return False

def handleEvent(state, event):  
    if (event.type == pg.MOUSEBUTTONDOWN):
        return(state[0], state[1], 0, 0)
        print("You Win")
    else:
        return(state)
   
initState = (400, 700, randint(-2,2),randint(-7,-3))
frameRate = 60

rw.runWorld(initState, updateDisplay, updateState, handleEvent, endState, frameRate)
