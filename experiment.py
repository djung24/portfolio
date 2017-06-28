from turtle import *

from random import randint 

dan = Turtle()

speed(0)

bgcolor('black')

def shape (number_of_sides):
    x = 1
    while x < 1000:

        r = randint(0, 250)
        g = randint(0, 250)
        b = randint(0, 250)
        colormode(255) 
        pencolor(r,g,b)
                
        forward(50 + x)
        right((360/number_of_sides) + .911)
        x = x+1

shape(6)

exitonclick() 






