import time
from turtle import Screen
from player import Player
from carmanager import Carmanager
from scoreboard import Board


screen = Screen()
screen.tracer(0)
screen.setup(600,600)
player = Player()
screen.title("Turtle Game")
screen.update()
screen.listen()

scoreboard = Board()

carmanager = Carmanager()
screen.onkey(player.moveup,"Up")
game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_car()
    carmanager.movecars()

    for car in carmanager.allcars:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()


    if player.isfinished():
        player.gotostart()
        carmanager.levelup()
        scoreboard.increase_level()






screen.exitonclick()