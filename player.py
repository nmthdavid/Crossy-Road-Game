from turtle import Turtle,Screen

STARTING_POSITION = (0,-280)
MOVE_DISTANCE = 10
FINSIH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def moveup(self):
        self.forward(MOVE_DISTANCE)

    def isfinished(self):
        if self.ycor() > 280:
            return True
        else:
            return False

    def gotostart(self):
        self.goto(STARTING_POSITION)