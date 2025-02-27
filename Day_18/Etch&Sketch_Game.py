from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# The Functions Used in the game
def Forwards():
    tim.forward(40)

def Backwards():
    tim.backward(40)


def Counter_Clockwise():
    new_heading = tim.heading() + 30
    tim.setheading(new_heading)
    


def Clockwise():
    new_heading = tim.heading() - 30
    tim.setheading(new_heading)


def Clear_Screen():
    tim.clear() 


screen.listen()
screen.onkeypress(key="w",fun=Forwards)
screen.onkey(key="s",fun=Backwards)
screen.onkey(key="a",fun=Counter_Clockwise)
screen.onkey(key="d",fun=Clockwise)
screen.onkey(key="c",fun=Clear_Screen)

screen.exitonclick()