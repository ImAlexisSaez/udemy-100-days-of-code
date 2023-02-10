import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = []


screen.listen()
screen.onkeypress(fun=player.up, key="Up")

loop_counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)

    # Create a car every 6th time the game loop runs
    if loop_counter % 6 == 0:
        cars.append(CarManager())

    # Move cars
    for car in cars:
        car.move()

    # Detect collision with car
    for car in cars:
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False

    # Detect turtle at finishing line
    if player.reached_top():
        player.next_level()
        scoreboard.level_up()
        for car in cars:
            car.speed_up()

    screen.update()
    loop_counter += 1

screen.exitonclick()
