import data
import random
import turtle as turtle_module

turtle_module.colormode(255)

tim = turtle_module.Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.penup()

screen = turtle_module.Screen()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(data.colors))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(50 * 10)
        tim.setheading(0)

screen.exitonclick()
