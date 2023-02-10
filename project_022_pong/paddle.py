from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(starting_position)

    def move_up(self):
        if self.ycor() < 240:
            self.sety(self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -240:
            self.sety(self.ycor() - 20)
