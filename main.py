import turtle
import random

wn = turtle.Screen()
#wn.bgcolor("Blue")
tess = turtle.Turtle()
#tcolor = input("Please input the color of the turtle")
tcolor = ("red")
tess.color(tcolor)
tess.speed(9)
tess.shape("turtle")
tess.penup() #this erases the lines

counter = 100
distance = 50
for x in range(counter):
    tess.stamp()
    tess.forward(distance)
    #tess.left(random.randrange(80,91))
    tess.left(85)
    distance += 2
