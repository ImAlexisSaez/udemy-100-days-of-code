from turtle import Turtle, Screen


def move_forwards():
    tim.forward(10)


tim = Turtle()
screen = Screen()
screen.listen()

# higher order function:
screen.onkey(key="space", fun=move_forwards)  # function as input

screen.exitonclick()
