# "colorgram is a pacakge i installed" : it is used to extract colors from any jpg image to use them
# import colorgram

# RGB_Colors = []
# Colors = colorgram.extract("HirstPainting.jpg", 30)     #this how it is work you give it the image and number of colors you need

# for color in Colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     RGB_Colors.append(new_color)

# print(RGB_Colors)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# "Color_list" This list i got it from copying the output of the previous code      
import turtle as turtle_module
import random


Color_list = [(226, 147, 98), (28, 102, 177), (161, 56, 90), (148, 79, 51), (225, 61, 96), (113, 174, 215), (244, 227, 95), (173, 20, 41), (233, 79, 51), (224, 126, 156), (118, 184, 130), (11, 172, 207), (165, 151, 25), (13, 58, 148), (83, 37, 23), (128, 37, 27), (37, 
129, 78), (42, 192, 160), (14, 39, 92), (129, 238, 190), (244, 162, 151), (235, 162, 181), (100, 101, 186), (127, 214, 239), (66, 77, 38), (74, 31, 46)]

turtle_module.colormode(255)
tim = turtle_module.Turtle()
screen = turtle_module.Screen()
tim.speed("fastest")
tim.penup()           # i used it because i do not need to draw the lines i just use "tim.dot()" to draw the dots
tim.hideturtle()      # this will hide the cursor

tim.setheading(225)   # imagine the screen of turtle is (x, y) planes this "225" represents the value of (x,y) as angle
tim.forward(300)      # now after getting the angle we need now we will move 300 move in this direction
tim.setheading(0)     # we put the angle to 0 again so that if we move we will move in (x-axis)  

number_of_dots = 100
for dot_count in range (1, number_of_dots + 1):
    tim.dot(30, random.choice(Color_list))
    tim.forward(50)
    # The next lines will put the cursor to the start of next line
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen.exitonclick()