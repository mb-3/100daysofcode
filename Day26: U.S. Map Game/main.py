import pandas
from states import State
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgpic("blank_states_img.gif")

with open("50_states.csv") as df:
    states_list = df.readlines()
    good_list = []
    for i in states_list:
        i_stripped = i.strip()
        if 'state' not in i_stripped:
            good_list.append(i_stripped.split(','))

correct_count = 0
answer = screen.textinput(title="Guess a state", prompt="Name a U.S. state:").title()
game_on = True

while game_on:
    if correct_count < 50:
        for state_item in good_list:
            if answer == state_item[0]:
                State(answer)
                correct_count += 1
    else:
        game_on = False
    answer = screen.textinput(title=f"States guessed: {correct_count}/50", prompt="What is another state?").title()

screen.mainloop()
