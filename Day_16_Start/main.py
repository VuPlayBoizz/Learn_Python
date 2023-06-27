import another_module

print(another_module.variable)
# Cach de khai bao 1 doi tuong c1
import turtle

timmy = turtle.Turtle()

print(timmy)

# Cach de khai bao 1 doi tuong c2
from turtle import Turtle

jymmy = Turtle()

print(jymmy)

jymmy.shape("turtle")

jymmy.color("blue")

jymmy.forward(100)

jymmy.right(90)

jymmy.forward(100)

# Doi tuong va thuoc tinh

from turtle import  Turtle, Screen

my_screen = Screen()

print(my_screen.canvheight)

# Doi tuong va phuong thuc

my_screen.exitonclick()

#Challenge

from prettytable import  PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmande"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "l"
print(table)
