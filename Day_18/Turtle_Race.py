from turtle import Turtle, Screen
import random

is_race_on = True

screen = Screen()
screen.setup(width = 500, height = 400)
User_Bet = screen.textinput(title="Make Your Bet: ", prompt="Which Turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
All_turtles = []
y = -140
for tur in range(0, 6):
    y += 40
    tim = Turtle(shape="turtle")
    tim.color(colors[tur])
    tim.penup()
    tim.goto(-230, y)
    All_turtles.append(tim)

while User_Bet not in colors:
    User_Bet = screen.textinput(title="Invalid Bet", prompt="Please enter a valid color (red, orange, yellow, green, blue, purple): ")


while is_race_on:
    for turtle in All_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == User_Bet:
                print(f"You Won! The {User_Bet} is the winning turtle")
            else:
                print(f"oops, You Lost! The {User_Bet} is the winning turtle")
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

screen.exitonclick()


