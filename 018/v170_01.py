import random
from turtle import Turtle, Screen

turtle = Turtle()
turtle.pensize(10)
turtle.speed("fast")

screen = Screen()
screen.colormode(255)  # To accept RGB colors

steps = random.randint(50, 100)

for step in range(steps):
    step_size = random.randint(15, 30)
    turtle_angle = random.randint(0, 359)
    turtle_color = tuple(random.randint(0, 255) for _ in range(3))
    turtle.pencolor(turtle_color)
    turtle.right(turtle_angle)
    turtle.forward(step_size)

screen.exitonclick()
