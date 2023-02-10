from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

for _ in range(10):
    turtle.forward(10)
    turtle.color(screen.bgcolor())
    turtle.forward(10)
    turtle.color("black")

turtle.right(90)
# Alternative
for _ in range(10):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

screen.exitonclick()
