from turtle import Turtle
import random
class Food(Turtle):                                            # I can inherit Class to another class by this way
    def __init__(self):                                        # Look how could i use the methods of Turtle in my class
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)       #this stretch the size
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

