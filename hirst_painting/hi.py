import math
import turtle

def xt(t):
    return 16*math.sin(t)**3

def yt(t):
    return 13*math.cos(t)-5*\
    math.cos(2*t)-2*\
    math.cos(3*t)-\
    math.cos(4*t)


t = turtle.Turtle()
t.hideturtle()
t.speed("fastest")
turtle.bgcolor("black")

for i in range(400):
    t.goto((xt(i)*20, yt(i)*20))
    t.pensize(1)
    t.pencolor("red")
    t.goto(0, 0)

def write(message, pos):
    x, y = pos
    t.penup()
    t.goto(x, y)
    t.color("pink")
    style = ('Cooper Black', 50, 'italic')
    t.write(message, font=style)

write('M', (-70, 0))
write('a', (-10, 0))
write('i', (30, 0))
write(' ', (55, 0))

screen = turtle.Screen()
screen.exitonclick()