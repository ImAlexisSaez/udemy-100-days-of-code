from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvwidth)
print(my_screen.canvheight)
my_screen.exitonclick()  # Así la ventana se cierra solo cuando pulsemos la X.
