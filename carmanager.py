import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "purple", "blue"]
STARTING_MOVE = 5

class Carmanager():

    def __init__(self):
        self.allcars = []
        self.carspeed = STARTING_MOVE

    def create_car(self):
        rand = random.randint(2,5)
        if rand == 4:
            newcar = Turtle("square")
            newcar.shapesize(stretch_wid=1,stretch_len=2)
            newcar.penup()
            newcar.color(random.choice(COLORS))
            randy = random.randint(-250,250)
            newcar.goto(300, randy)
            self.allcars.append(newcar)

    def movecars(self):
        for car in self.allcars:
            car.backward(self.carspeed)

    def levelup(self):
        self.carspeed += 5
