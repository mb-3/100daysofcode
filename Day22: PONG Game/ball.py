from turtle import Turtle

SHAPE = "circle"
COLOR = "white"
STARTING_POS = (0, 0)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.shape(SHAPE)
        self.penup()
        self.goto(STARTING_POS)
        self.going_right = True
        self.going_up = True
        self.move_speed = 0.1

    def move(self):
        if self.ycor() >= 280:
            self.going_up = False
        if self.ycor() <= -280:
            self.going_up = True

        if self.going_up:
            new_y = self.ycor() + 10
        else:
            new_y = self.ycor() - 10

        if self.going_right:
            new_x = self.xcor() + 10
        else:
            new_x = self.xcor() - 10

        self.goto(new_x, new_y)

    def reset_ball(self):
        if self.xcor() < -395:
            self.goto(0, 0)
            self.going_right = True
        elif self.xcor() > 395:
            self.goto(0, 0)
            self.going_right = False

        self.move_speed = 0.1

