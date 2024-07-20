from turtle import Turtle, Screen
turtle = Turtle()
turtle_2 = Turtle()
turtle_2.penup()
turtle_2.shape()

screen = Screen()

screen.title("This is US states guessing game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
import csv
import pandas
def ask_input():

    return(input_states)

guessed_state = []
with open("./50_states.csv") as get_cor:
    data = pandas.read_csv(get_cor)
    states_name = data["state"].to_list()
    length = len(data)


    while len(guessed_state) < 50:
        input_states = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's the state name?").title()
        user_input = ask_input()
        if user_input in states_name:
            guessed_state.append(user_input)
            index = data[data.state == user_input]
            turtle_2.goto((int(index.x), int(index.y)))
            turtle_2.pendown()
            turtle_2.write(user_input, False, font=("Arial", 8, "normal"))
            turtle_2.penup()
        elif user_input == "Exit":
            missing = [state for state in states_name if state not in guessed_state]
            new_data = pandas.DataFrame(missing)
            new_data.to_csv("states_to_learn")
            break

        else:

            print("State Not found, next guess!!!")


turtle.screen.mainloop()



