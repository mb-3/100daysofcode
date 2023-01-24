from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.going_right = False
        ball.move_speed *= 0.9
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.going_right = True
        ball.move_speed *= 0.9

    if ball.xcor() < -395:
        ball.reset_ball()
        scoreboard.r_point()
        scoreboard.update_scoreboard()

    elif ball.xcor() > 395:
        ball.reset_ball()
        scoreboard.l_point()
        scoreboard.update_scoreboard()

screen.exitonclick()
