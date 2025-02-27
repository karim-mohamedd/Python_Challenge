from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# The Functions Used in the game
def Forwards():
    tim.forward(20)

def Backwards():
    tim.backward(20)

def Counter_Clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def Clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def Clear_Screen():
    tim.clear()

# Key flags to track key presses
key_state = {
    "w": False,
    "s": False,
    "a": False,
    "d": False
}

# Update the movement functions to repeat when the key is held down
def move():
    if key_state["w"]:
        Forwards()
    if key_state["s"]:
        Backwards()
    if key_state["a"]:
        Counter_Clockwise()
    if key_state["d"]:
        Clockwise()
    screen.ontimer(move, 100)  # Repeat this function every 100ms

# Key press functions
def press_w():
    key_state["w"] = True

def press_s():
    key_state["s"] = True

def press_a():
    key_state["a"] = True

def press_d():
    key_state["d"] = True

# Key release functions
def release_w():
    key_state["w"] = False

def release_s():
    key_state["s"] = False

def release_a():
    key_state["a"] = False

def release_d():
    key_state["d"] = False

# Listen for key presses and releases
screen.listen()
screen.onkey(press_w, "w")
screen.onkey(press_s, "s")
screen.onkey(press_a, "a")
screen.onkey(press_d, "d")
screen.onkey(release_w, "w")
screen.onkey(release_s, "s")
screen.onkey(release_a, "a")
screen.onkey(release_d, "d")
screen.onkey(Clear_Screen, "c")

# Start the movement loop
move()

screen.exitonclick()
