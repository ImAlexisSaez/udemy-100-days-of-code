from turtle import Turtle, Screen


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def rotate_counter_clockwise():
    tim_heading = tim.heading()
    tim.setheading(tim_heading + 10)


def rotate_clockwise():
    tim_heading = tim.heading()
    tim.setheading(tim_heading - 10)


def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


tim = Turtle()
screen = Screen()
screen.listen()

# higher order function:
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_counter_clockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()
