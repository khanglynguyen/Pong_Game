from ball import Ball
from slider import Slider
from scoreboard import Scoreboard
from turtle import Screen
import time
R_POS = (350,0)
L_POS = (-350,0)
HEIGHT = 600
WIDTH = 800
screen = Screen()
screen.bgcolor("black")
screen.setup(height= HEIGHT, width= WIDTH)
screen.title("Pong")
screen.tracer(0)

r_slider = Slider(R_POS)
l_slider = Slider(L_POS)
ball = Ball()
scoreboard = Scoreboard()
game_on = True

screen.onkeypress(r_slider.go_up, "Up")
screen.onkeypress(r_slider.go_down, "Down")
screen.onkeypress(l_slider.go_up, "w")
screen.onkeypress(l_slider.go_down, "s")
screen.listen()

while game_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()
    x = ball.heading()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_cell()
    if ball.xcor() >320 and ball.distance(r_slider)< 50:
        ball.bounce_slider()
    elif ball.xcor() < -320 and ball.distance(l_slider) < 50:
        ball.bounce_slider()
    # if ball.xcor() >330 and ball.distance(r_slider)< 50 or ball.xcor() < -330 and ball.distance(l_slider) < 50:
    #       ball.bounce_slider()
    if ball.xcor() > 380:
        scoreboard.l_update()
        scoreboard.update()
        ball.restart()
        time.sleep(1.5)
    elif ball.xcor() < -380:
        scoreboard.r_update()
        scoreboard.update()
        ball.restart()
        time.sleep(1.5)
























screen.exitonclick()