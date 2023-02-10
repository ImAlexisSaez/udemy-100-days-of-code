import pandas
import turtle

# Read the data
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

# Configure screen
screen = turtle.Screen()
screen.title("U.S. States Game")
bg_image = "blank_states_img.gif"
screen.addshape(bg_image)
turtle.shape(bg_image)

# Game settings
states_correct = 0
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(
        title=f"{states_correct} / 50 States Correct",
        prompt="What's another state?"
    ).title()

    if answer == "Exit":
        break

    if answer in all_states:
        guessed_states.append(answer)
        states_correct += 1
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        x_coord = int(data[data["state"] == answer].x)
        y_coord = int(data[data["state"] == answer].y)
        t.goto(x_coord, y_coord)
        t.write(answer)

states_to_learn = [state for state in all_states if state not in guessed_states]
states_to_learn = pandas.DataFrame(states_to_learn)
states_to_learn.to_csv("states_to_learn.csv")
