from turtle import Turtle, Screen
import random
Colors = ["cornflower blue","red","blue","black","aquamarine","firebrick","blue violet","indigo","chocolate","yellow green","gold","dark green","olive drab"]
turtle_1 = Turtle()
turtle_1.speed(2)
screen_1 = Screen()
# Draw different shapes
def Draw_Shapes():
    degree = 360
    for slides in range(3, 12):
        new_degree = degree / slides
        turtle_1.color(random.choice(Colors))
        for _ in range(slides):
            turtle_1.forward(100)
            turtle_1.left(new_degree)
Draw_Shapes()
screen_1.exitonclick()

            


