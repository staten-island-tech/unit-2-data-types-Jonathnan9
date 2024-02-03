import turtle
from turtle import *

t = Turtle()
t.speed(0)

print("wow no errors")

length=5

def Square(length):
    for i in range(4):
        t.forward(length)
        t.right(90)

def SQuareSpiral(iRange):
    length = 5
    for i in range(iRange):
        Square(length)
        length += 5
        t.right(5)
SQuareSpiral(60)

turtle.done()