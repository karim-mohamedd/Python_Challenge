from turtle import Turtle, Screen
from snake import Snake
import time
# Setting the screen 
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")

# Creating the default start of the game (3 segments of white snake each is 20x20 size)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
















screen.exitonclick()