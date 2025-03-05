from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)
    
    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)

    def Game_Over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over", align = ALIGNMENT, font = FONT)
