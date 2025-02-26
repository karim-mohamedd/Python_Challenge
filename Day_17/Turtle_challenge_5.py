import turtle as t   # Notice here i did add " as t " to be able to edit on t module itself
import random        # I Can not use "pencolor()" to take a set of numbers before editing the colormode to 255 

t.colormode(255)     # Here i did edit on the module itself and changed the colormode to 255
tim = t.Turtle()

# selecting the options for the turtle
tim.pensize(12)
tim.speed(5)
tim.pensize(10)

def Random_Color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270]

for i in range (200):
    tim.seth(random.choice(directions))
    tim.forward(50)
    tim.pencolor(Random_Color())




