import random
from turtle import Turtle, Screen

colors = ["red", "orange", "yellow", "green","blue", "purple"]
is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which color will win the race?\n"
           "(red / orange / yellow / green / blue / purple)\n"
           "Enter a color: "
).lower()

x_positions = -230
y_positions = [-125, -75, -25, 25, 75, 125]
race_turtles = []

for turtle_index in range(6):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[turtle_index])
    turtle.goto(x=x_positions, y=y_positions[turtle_index])
    race_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for race_turtle in race_turtles:
        # turtles are 40x40, so, 250 - 40/2 = 230
        if race_turtle.xcor() >= 230:
            is_race_on = False
            winning_color = race_turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
            break
        race_turtle.forward(random.randint(1, 10))

screen.exitonclick()
