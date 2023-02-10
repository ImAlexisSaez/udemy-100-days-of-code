from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snake = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
for position in starting_positions:
    turtle = Turtle(shape="square")
    turtle.color("white")
    turtle.penup()
    turtle.goto(position)
    snake.append(turtle)

screen.exitonclick()
