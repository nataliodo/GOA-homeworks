from turtle import *

#we want to paint a house

#step 1: draw a square
speed(30)
width(7)
color("orange")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color("blue")
right(150)
forward(200)
left(120)
forward(200)
color("orange")
left(30)
forward(100)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
penup()
goto(200, 200)
pendown()
left(90)
forward(100)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
exitonclick()
