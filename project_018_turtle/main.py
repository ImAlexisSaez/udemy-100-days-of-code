import colorgram
import random

from turtle import Turtle, Screen


def get_colors(image, num_colors):
    list_of_colors = []
    image_colors = colorgram.extract(image, num_colors)

    for color in image_colors:
        red = color.rgb.r
        green = color.rgb.g
        blue = color.rgb.b
        list_of_colors.append((red, green, blue))

    return list_of_colors[4:]  # Leave first colors (white background colors).


dot_size = 20
turtle_step = 50
image_path = "image.jpg"
number_of_colors = 30

turtle = Turtle(visible=False)
turtle.speed("fastest")

screen = Screen()
screen.colormode(255)  # To accept RGB colors
screen_width, screen_height = screen.screensize()

colors = get_colors(image_path, number_of_colors)

turtle_y = -dot_size - screen_height
for y_step in range(10):
    turtle_x = dot_size - screen_width
    for x_step in range(10):
        turtle.penup()
        turtle.goto(turtle_x, turtle_y)
        turtle.pendown()
        turtle.dot(dot_size, random.choice(colors))
        turtle_x += turtle_step
    turtle_y += turtle_step

screen.exitonclick()



