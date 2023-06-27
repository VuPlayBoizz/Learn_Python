from turtle import Turtle, Screen
import random


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("orchid")
for i in range(15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()

colours = ["spring green", "orange red", "deep sky blue", "pink", "blue violet", "medium purple", "light salmon"]
shape = Turtle()
def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        shape.forward(100)
        shape.right(angle)

for shape_side_n in range(3, 11):
    shape.pensize(10)
    shape.color(random.choice(colours))
    draw_shape(shape_side_n)


import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
