from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def up(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

    def reached_top(self):
        return self.ycor() >= FINISH_LINE_Y

    def next_level(self):
        self.goto(STARTING_POSITION)