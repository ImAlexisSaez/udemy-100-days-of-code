import time
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from turtle import Screen

r_paddle = Paddle((350, 0))  # Right paddle
l_paddle = Paddle((-350, 0))  # Left paddle
ball = Ball()
scoreboard = Scoreboard()
screen = Screen()

screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

screen.listen()
screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")
screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if abs(ball.ycor()) > 280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right paddle misses
    if ball.xcor() > 380:
        scoreboard.increase_l_score()
        ball.reset_position()

    # Detect left paddle misses
    if ball.xcor() < -380:
        scoreboard.increase_r_score()
        ball.reset_position()



screen.exitonclick()
