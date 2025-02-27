from turtle import Turtle, Screen
import random

is_race_on = True

screen = Screen()
screen.setup(width = 500, height = 400)          # Setting the options for Screen
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

# Validation that the user will input right color
while User_Bet not in colors:
    User_Bet = screen.textinput(title="Invalid Bet", prompt="Please enter a valid color (red, orange, yellow, green, blue, purple): ")


while is_race_on:
    for turtle in All_turtles:
        if turtle.xcor() > 230:                  # "xcor()" stand for x-coordinate
            is_race_on = False
            winning_color = turtle.pencolor()    # This to capture the wining turtle
            turtle.hideturtle()                  # This will hide the turtle after arriving to end
            if winning_color == User_Bet:
                turtle.setpos(0,170)             # The first argument is X-axis and the second is Y-axis setpos for setposition
                turtle.write(f"You Won !! {winning_color} is The winning turtle", align="center", font=("Arial", 12, "bold"))
            else:
                turtle.setpos(0,170)
                turtle.write(f"oops, You Lost ! The {winning_color} is The winning turtle", align="center", font=("Arial", 12, "bold"))
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

screen.exitonclick()



