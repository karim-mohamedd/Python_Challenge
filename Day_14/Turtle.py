import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle object
pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(1)

# Function to draw a heart shape
def draw_heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(50)
    pen.forward(133)
    pen.circle(50, 200)
    pen.right(140)
    pen.circle(50, 200)
    pen.forward(133)
    pen.end_fill()

# Draw the heart shape
pen.penup()
pen.goto(0, -150)
pen.pendown()
draw_heart()

# Write the message
pen.penup()
pen.goto(0, 50)
pen.pendown()
pen.color("black")
pen.write("Happy Valentine Day Salma", align="center", font=("Arial", 18, "bold"))

# Hide the turtle after drawing
pen.hideturtle()

# Keep the window open
turtle.done()
