import random
from turtle import Turtle, Screen

turtle = Turtle()
turtle.pensize(1)
turtle.speed("fastest")
angle = 0

screen = Screen()
screen.colormode(255)  # To accept RGB colors

for _ in range(90):
    turtle_color = tuple(random.randint(0, 255) for _ in range(3))
    turtle.pencolor(turtle_color)
    turtle.circle(100)
    turtle.right(angle + 4)

screen.exitonclick()
