from turtle import Turtle, Screen
from paddle import *
from ball import Ball
from scoreboard import Scoreboard
import time


#setting the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)


#
paddle_r = Paddle(RIGHT)
paddle_l = Paddle(LEFT)
ball = Ball()
score_board = Scoreboard()

screen.listen()

screen.onkey(paddle_r.go_up,"Up" )
screen.onkey(paddle_r.go_down,"Down")
screen.onkey(paddle_l.go_up,"w" )
screen.onkey(paddle_l.go_down,"s")

is_on = True
while is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detecting collision with ball
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    #detecting collision with right paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #detecting if misses right
    if ball.xcor() > 380 :
        ball.reset_position()
        score_board.l_point()
    #detecting if misses left
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()


screen.exitonclick()