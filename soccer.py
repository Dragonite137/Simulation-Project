import runWorld as rw
import drawWorld as dw
import pygame as pg
from random import randint

name = "Move the cursor over the Soccer Ball to Stop it from Going in the Goal!"
width = 800
height = 800
rw.newDisplay(width, height, name)

myimage = dw.loadImage("soccer_ball_1.bmp")
goal = dw.loadImage("goal.bmp")

class State:
    xpos = 400
    ypos = 700
    xvel = randint(-2,2)
    yvel = randint(-12,-10)
    def move(self):
        self.xpos = self.xpos + self.xvel
        self.ypos = self.ypos + self.yvel
    
initState = State()

def updateDisplay(state):
    dw.fill(dw.white)
    dw.draw(goal, (0, 0, 0, 0))
    dw.draw(myimage, (state.xpos, state.ypos, state.xvel, state.yvel))

def updateState(state):
    state.move()
    return (state)

def endState(state):
    if ((state.xpos > width or state.xpos < 0 or state.ypos > height or state.ypos < 0) or (state.xvel==0 and state.yvel==0)):
        return True
    else:
        return False

def handleEvent(state, event):
    p = pg.mouse.get_pos()
    if ((p[0]>=state.xpos and p[0] <= (state.xpos + 98)) and  ((p[1]>=state.ypos and p[1] <= (state.ypos + 100)))):
        state.xvel = 0
        state.yvel = 0
        return(state)
    else:
        return(state)
   
#initState = (400, 700, randint(-2,2),randint(-12,-10))

frameRate = 60

rw.runWorld(initState, updateDisplay, updateState, handleEvent, endState, frameRate)
