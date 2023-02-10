import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.car_speed = STARTING_MOVE_DISTANCE
        self.sety(random.randrange(-250, 250))
        self.setx(300)

    def move(self):
        self.setx(self.xcor() - self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT

