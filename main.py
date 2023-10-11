import turtle
import pandas as pd

#Importing the library
data = pd.read_csv("50_states.csv")

#setting up the screen
screen = turtle.Screen()
screen.title("US States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
#pulling the information from the csv
states_list = data.state.to_list()

#Continue to ask the user
count = 0
answer_list = []


while count <= 51:
    if answer_list != states_list:
        # screen prompt
        answer = screen.textinput(title=f"{count}/51 Guess the state", prompt="Write a state name: ")
        answers = answer.title()

    if answer == "exit" or answers == "Exit":
        wrong_answer_list = []
        for answers in states_list:
            if answers not in answer_list:
                wrong_answer_list.append(answers)
        to_learn = pd.DataFrame(wrong_answer_list)
        to_learn.to_csv("To_learn.csv")

        screen.bye()

#check if the answer matches the states_list and print the answer
    if answers in states_list:
        answer_list.append(answers)
        count += 1
        typo = turtle.Turtle()
        typo.hideturtle()
        typo.penup()
        stated = data[data.state == answers]
        typo.goto(int(stated.x), int(stated.y))
        typo.pendown()
        typo.write(answers)

#Finding the coordinates of the map for each location of state
#def get_coordinates(x, y):
#    print(x, y)

#turtle.onscreenclick(get_coordinates())


