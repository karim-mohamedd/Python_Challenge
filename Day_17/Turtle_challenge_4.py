from turtle import Turtle, Screen
import random
Colors = ["cornflower blue","red","blue","black","aquamarine","firebrick","blue violet","indigo","chocolate","yellow green","gold","dark green","olive drab"]
walks = [0,90,180,270]
tur_1 = Turtle()
tur_1.pensize(10)
screen_1 = Screen()
# selecting the options for the turtle
tur_1.pensize(12)
tur_1.speed(5)
for i in range (200):
    tur_1.seth(random.choice(walks))
    tur_1.forward(50)
    tur_1.color(random.choice(Colors))


screen_1.exitonclick()