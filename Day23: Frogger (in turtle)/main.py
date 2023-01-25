import time
from turtle import Screen
from player import Player
from car_manager import CarManager, car_fleet
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car = CarManager()
score = Scoreboard()

screen.onkey(player.move, "Up")

game_is_on = True
counter = 0
while game_is_on:
    counter += 1
    time.sleep(0.1)
    screen.update()
    car.move()
    # Generates a car every .6 seconds
    if counter == 6:
        car.generate()
        counter = 0

    # Ends game if contact is made
    for i in car_fleet:
        if i.distance(player) < 22:
            score.game_over()
            game_is_on = False

    # If player reaches top of screen, add 1 to level, speed up cars, reset player's position
    if player.finish_line():
        car.level_up()
        score.level_up()
        player.reset_pos()

screen.exitonclick()
