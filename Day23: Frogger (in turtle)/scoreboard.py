from turtle import Turtle

FONT = ("Courier", 20, "bold")
ALIGNMENT = "left"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-290, 260)
        self.hideturtle()
        self.color("black")
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)
