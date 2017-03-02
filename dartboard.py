import turtle
import math
wn = turtle.Screen()
luc = turtle.Turtle()
luc.speed(100000)
distance = 6
posY = -260
posX = 0
def  circle():
    for i in range(360):
        luc.fd(distance)
        luc.lt(1)

thisis a sentence

for i in range(6):
    luc.pu()
    luc.goto(posX,posY)
    luc.pd()
    circle()
    distance -= 1
    posY  += 54
    

