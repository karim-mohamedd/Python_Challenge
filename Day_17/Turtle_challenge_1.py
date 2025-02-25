from turtle import Turtle, Screen

Turtle_1 = Turtle()
Turtle_1.speed(2)
screen_1 = Screen()
#Draw a square
def draw_square():
    for i in range(4):
        Turtle_1.forward(100)
        Turtle_1.left(90)
    screen_1.exitonclick()
    

draw_square()