import random
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
screen.colormode(255)  # To accept RGB colors

step = 100
for sides in range(4, 11):
    angle = 360 / sides
    turtle_color = tuple(random.randint(0, 255) for _ in range(3))
    for _ in range(sides):
        turtle.pencolor(turtle_color)
        turtle.forward(step)
        turtle.right(angle)

screen.exitonclick()
