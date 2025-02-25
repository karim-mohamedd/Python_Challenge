from turtle import Turtle, Screen

#Draw a dashed line of 10 paces and gap of 10 paces

turtle_1 = Turtle()
turtle_1.shape("arrow")
turtle_1.speed(2)
screen_1 = Screen()

def draw_dashed_line():
    for _ in range(15):
        turtle_1.forward(10)
        turtle_1.penup()
        turtle_1.forward(10)
        turtle_1.pendown()


draw_dashed_line()
screen_1.exitonclick()