import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed("fastest")
tim.pensize(4)

def draw_spino(size):
    for i in range(int(360 / size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size)

draw_spino(5)

screen = Screen()
screen.exitonclick()
