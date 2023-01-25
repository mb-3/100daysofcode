from turtle import Turtle
import random
import time

car_fleet = []
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LEFT = 180


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(320, random.randint(-250, 250))
        self.setheading(LEFT)
        self.level = 0

    def generate(self):
        car_fleet.append(CarManager())

    def move(self):
        for i in car_fleet:
            i.forward(STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * self.level))

    def level_up(self):
        self.level += 1


