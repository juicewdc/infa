from turtle import *
r=15
tracer(0)
screensize(1920,1080)
right(90)
pendown()
for i in range(2):
    forward(5*r)
    left(90)
    back(13*r)
    left(90)
penup()
back(10*r)
right(90)
forward(9*r)
left(90)
pendown()
for i in range(2):
    forward(11*r)
    right(90)
    forward(7*r)
    right(90)
penup()
for x in range(-10, 10):
    for y in range(-10, 10):
        setpos(x*40, y*40)
        dot(1, 'red')

done()