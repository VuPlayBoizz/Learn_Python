from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle = Turtle()
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name ?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        new_turtle = Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        state_data = data[data.state == answer_state]
        new_turtle.goto(int(state_data.x), int(state_data.y))
        new_turtle.write(answer_state)


