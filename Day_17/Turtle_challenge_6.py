import turtle as t   # Notice here i did add " as t " to be able to edit on the module itself
import random        # I Can not use "pencolor()" to take a set of numbers before editing the colormode to 255 

t.colormode(255)     # Here i did edit on the module itself and changed the colormode to 255
tim = t.Turtle()
screen = t.Screen()
# selecting the options for the turtle

tim.speed("fastest")


def Random_Color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def Draw_SpiroGraph(size_of_gap):
    for _ in range (int(360 / size_of_gap)):
        tim.color(Random_Color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.seth(current_heading + size_of_gap)

Draw_SpiroGraph(4)   #here we pass the gap size s parameter
screen.exitonclick()