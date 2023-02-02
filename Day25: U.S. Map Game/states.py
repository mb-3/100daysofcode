from turtle import Turtle
import pandas

with open("50_states.csv") as df:
    states_list = df.readlines()
    good_list = []
    for i in states_list:
        i_stripped = i.strip()
        if 'state' not in i_stripped:
            good_list.append(i_stripped.split(','))


class State(Turtle):

    def __init__(self, state_name):
        super().__init__()
        self.name = state_name
        self.hideturtle()
        self.penup()
        self.color("black")
        for state_item in good_list:
            if state_item[0] == self.name:
                self.goto(int(state_item[1]), int(state_item[2]))
                self.write(f"{state_name}", align="center", font=("Courier", 8, "normal"))



