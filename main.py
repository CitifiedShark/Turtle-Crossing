import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# detect player movements
screen.listen()
screen.onkey(player.move, "Up")
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()

    car_manager.spawn_car()
    car_manager.move_car()

    if player.player.ycor() >= 280:
        player.next_level()
        car_manager.next_level()
        scoreboard.next_level()

    for car in car_manager.cars:
        if car.distance(player.player) < 20:
            scoreboard.game_is_over()
            game_is_on = False

screen.exitonclick()
