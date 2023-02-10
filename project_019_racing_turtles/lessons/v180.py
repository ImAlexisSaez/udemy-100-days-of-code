from turtle import Turtle, Screen

colors = ["red", "orange", "yellow", "green","blue", "purple"]

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

screen.exitonclick()
